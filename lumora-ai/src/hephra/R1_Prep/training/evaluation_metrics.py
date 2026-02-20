import os
import io
import time
import json
import base64
import requests
import pdfplumber
from openai import OpenAI
from dotenv import load_dotenv
import re
from typing import Dict, List, Any

# Load all env
load_dotenv()

# Create Client
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


# ============================================================================
# PDF PROCESSING FUNCTIONS
# ============================================================================

def download_pdf_bytes(file_url):
    """
    Download PDF from URL and return bytes

    Args:
        file_url (str): URL of the PDF file

    Returns:
        bytes: PDF file content as bytes
    """
    response = requests.get(file_url)
    response.raise_for_status()
    return response.content


def get_text_from_pdf(file_url):
    """
    Extract text content from PDF using pdfplumber

    Args:
        file_url (str): URL of the PDF file

    Returns:
        str: Extracted text from all pages
    """
    pdf_bytes = download_pdf_bytes(file_url)
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf_file:
        pdf_text = "\n".join([page.extract_text() for page in pdf_file.pages])
    return pdf_text


def get_pdf_base64(file_url):
    """
    Download PDF and encode in base64 (for direct PDF API input)

    Args:
        file_url (str): URL of the PDF file

    Returns:
        str: Base64 encoded PDF content
    """
    pdf_bytes = download_pdf_bytes(file_url)
    pdf_base64 = base64.b64encode(pdf_bytes).decode("utf-8")
    return pdf_base64


# ============================================================================
# IMPROVED PROMPT FOR BETTER SCALING
# ============================================================================

def create_extraction_prompt(pdf_text):
    """
    Create an improved prompt with complete schema and clear instructions
    This version scales better across different document types

    Args:
        pdf_text (str): Extracted text from PDF

    Returns:
        str: Formatted prompt for LLM
    """
    my_prompt = f"""
You are a medical data extraction software.
Extract structured data from the provided medical lab report text.

RULES:
- Output ONLY valid JSON, no markdown code blocks or commentary
- Use null for missing fields (never leave fields undefined)
- Dates must be in YYYY-MM-DD format
- If multiple patients exist, extract only the first one
- If extraction completely fails, return {{"error": "reason for failure"}}
- Extract ALL lab tests found in the report

REQUIRED JSON STRUCTURE:
{{
  "patient_name": "string or null",
  "date_of_birth": "YYYY-MM-DD or null",
  "report_date": "YYYY-MM-DD or null",
  "ordering_physician": "string or null",
  "lab_tests": [
    {{
      "test_name": "string",
      "value": "string or number",
      "unit": "string or null",
      "reference_range": "string or null",
      "status": "normal|abnormal|critical or null"
    }}
  ]
}}

TEXT:
{pdf_text}
"""
    return my_prompt


# ============================================================================
# MAIN EXTRACTION FUNCTION
# ============================================================================

def get_data(file_name, file_url):
    """
    Extract medical data from PDF using LLM

    Args:
        file_name (str): Name identifier for the file
        file_url (str): URL of the PDF file

    Returns:
        dict: Extracted data in JSON format
    """
    # Get text from pdf
    pdf_text = get_text_from_pdf(file_url)

    # Create prompt with improved structure
    my_prompt = create_extraction_prompt(pdf_text)

    print(f"Extraction for {file_name}.pdf in progress...")

    # Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,  # 0 for deterministic outputs
        messages=[{"role": "user", "content": my_prompt}]
    )

    # Parse JSON response
    try:
        data = json.loads(response.choices[0].message.content)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        data = {"error": "Failed to parse LLM response as JSON"}

    return data


# ============================================================================
# EVALUATION METRICS - ACCURACY
# ============================================================================

def evaluate_extraction(predicted: Dict, ground_truth: Dict) -> Dict:
    """
    Compare predicted output against ground truth to measure accuracy

    Args:
        predicted (dict): LLM extracted data
        ground_truth (dict): Known correct data

    Returns:
        dict: Metrics including field-level accuracy and overall score
    """
    metrics = {
        "exact_match": predicted == ground_truth,
        "field_accuracy": {},
        "missing_fields": [],
        "extra_fields": [],
        "incorrect_fields": []
    }

    # Check each field in ground truth
    for field in ground_truth.keys():
        if field not in predicted:
            metrics["missing_fields"].append(field)
            metrics["field_accuracy"][field] = 0.0
        elif predicted[field] == ground_truth[field]:
            metrics["field_accuracy"][field] = 1.0
        else:
            metrics["field_accuracy"][field] = 0.0
            metrics["incorrect_fields"].append({
                "field": field,
                "expected": ground_truth[field],
                "got": predicted[field]
            })

    # Check for extra fields not in ground truth
    for field in predicted.keys():
        if field not in ground_truth:
            metrics["extra_fields"].append(field)

    # Calculate overall accuracy (excluding extra fields)
    if metrics["field_accuracy"]:
        metrics["overall_accuracy"] = sum(metrics["field_accuracy"].values()) / len(ground_truth)
    else:
        metrics["overall_accuracy"] = 0.0

    return metrics


def calculate_precision_recall(predicted_fields: List[str], actual_fields: List[str]) -> Dict:
    """
    Calculate precision, recall, and F1 score for field extraction

    Precision: Of the fields we extracted, how many were correct?
    Recall: Of the fields that exist, how many did we extract?
    F1: Harmonic mean of precision and recall

    Args:
        predicted_fields (list): Fields extracted by LLM
        actual_fields (list): Fields that actually exist

    Returns:
        dict: Precision, recall, and F1 scores
    """
    predicted_set = set(predicted_fields)
    actual_set = set(actual_fields)

    true_positives = len(predicted_set & actual_set)  # Correctly extracted
    false_positives = len(predicted_set - actual_set)  # Extracted but don't exist
    false_negatives = len(actual_set - predicted_set)  # Exist but not extracted

    # Calculate metrics
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    return {
        "precision": precision,
        "recall": recall,
        "f1_score": f1_score,
        "true_positives": true_positives,
        "false_positives": false_positives,
        "false_negatives": false_negatives
    }


# ============================================================================
# VALIDATION FUNCTIONS
# ============================================================================

def validate_llm_output(output_data: Any, source_text: str = "") -> Dict:
    """
    Validate the quality and format of LLM output

    Args:
        output_data: The extracted data (should be dict)
        source_text (str): Original text to check for hallucinations

    Returns:
        dict: Validation results with boolean flags
    """
    validations = {
        "is_valid_json": False,
        "is_dict": False,
        "has_all_required_fields": False,
        "date_format_correct": True,  # Assume true until proven false
        "has_error_field": False,
        "no_markdown_artifacts": True
    }

    # Check if it's a dictionary (already parsed JSON)
    if isinstance(output_data, dict):
        validations["is_valid_json"] = True
        validations["is_dict"] = True
        data = output_data
    else:
        return validations

    # Check for error field
    if "error" in data:
        validations["has_error_field"] = True
        return validations

    # Check required fields
    required_fields = ["patient_name", "date_of_birth", "report_date", "ordering_physician", "lab_tests"]
    validations["has_all_required_fields"] = all(field in data for field in required_fields)

    # Validate date formats (YYYY-MM-DD)
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'
    date_fields = ["date_of_birth", "report_date"]

    for field in date_fields:
        if field in data and data[field] is not None:
            if not re.match(date_pattern, str(data[field])):
                validations["date_format_correct"] = False
                break

    # Check lab_tests structure
    if "lab_tests" in data and isinstance(data["lab_tests"], list):
        for test in data["lab_tests"]:
            if not isinstance(test, dict):
                validations["has_all_required_fields"] = False
                break

    return validations


def calculate_success_rate(test_results: List[Dict]) -> float:
    """
    Calculate the percentage of successful extractions

    Args:
        test_results (list): List of test result dictionaries

    Returns:
        float: Success rate (0.0 to 1.0)
    """
    if not test_results:
        return 0.0

    successful = sum(
        1 for r in test_results
        if r.get("valid_json", False) and r.get("has_required_fields", False)
    )
    total = len(test_results)

    return successful / total


# ============================================================================
# PERFORMANCE METRICS
# ============================================================================

def measure_performance(test_cases: List[Dict]) -> Dict:
    """
    Measure performance metrics like latency across multiple test cases

    Args:
        test_cases (list): List of test case dictionaries with 'name' and 'url'

    Returns:
        dict: Performance metrics including latency statistics
    """
    results = {
        "avg_latency": 0,
        "max_latency": 0,
        "min_latency": float('inf'),
        "latencies": [],
        "total_time": 0
    }

    latencies = []
    start_total = time.time()

    for test in test_cases:
        start = time.time()
        try:
            response = get_data(test["name"], test["url"])
            latency = time.time() - start
            latencies.append(latency)
        except Exception as e:
            print(f"Error processing {test['name']}: {e}")
            latencies.append(0)

    results["total_time"] = time.time() - start_total
    results["latencies"] = latencies

    if latencies:
        results["avg_latency"] = sum(latencies) / len(latencies)
        results["max_latency"] = max(latencies)
        results["min_latency"] = min(latencies)

    return results


# ============================================================================
# COMPREHENSIVE EVALUATION
# ============================================================================

def full_evaluation(test_suite: List[Dict]) -> Dict:
    """
    Run comprehensive evaluation across all test cases

    Args:
        test_suite (list): List of test cases with optional ground_truth
            Example: [
                {
                    "name": "test1",
                    "url": "http://...",
                    "ground_truth": {...}  # Optional
                }
            ]

    Returns:
        dict: Complete evaluation results with all metrics
    """
    results = {
        "accuracy_scores": [],
        "validation_results": [],
        "performance_metrics": {},
        "error_analysis": {
            "parsing_errors": 0,
            "missing_fields": 0,
            "incorrect_values": 0,
            "total_tests": len(test_suite)
        },
        "detailed_results": []
    }

    print(f"\n{'=' * 60}")
    print(f"Running evaluation on {len(test_suite)} test cases...")
    print(f"{'=' * 60}\n")

    for i, test_case in enumerate(test_suite):
        print(f"[{i + 1}/{len(test_suite)}] Processing: {test_case['name']}")

        test_result = {
            "name": test_case["name"],
            "success": False,
            "validation": {},
            "accuracy": None
        }

        try:
            # Run extraction
            start_time = time.time()
            predicted = get_data(test_case["name"], test_case["url"])
            extraction_time = time.time() - start_time

            test_result["extraction_time"] = extraction_time

            # Validate output quality
            validation = validate_llm_output(predicted)
            test_result["validation"] = validation
            results["validation_results"].append(validation)

            # Check for errors
            if not validation["is_valid_json"]:
                results["error_analysis"]["parsing_errors"] += 1
            if not validation["has_all_required_fields"]:
                results["error_analysis"]["missing_fields"] += 1

            # Compare with ground truth if available
            if "ground_truth" in test_case:
                accuracy = evaluate_extraction(predicted, test_case["ground_truth"])
                test_result["accuracy"] = accuracy
                results["accuracy_scores"].append(accuracy["overall_accuracy"])

                if accuracy["incorrect_fields"]:
                    results["error_analysis"]["incorrect_values"] += len(accuracy["incorrect_fields"])

            # Mark as successful if valid JSON and has required fields
            test_result["success"] = validation["is_valid_json"] and validation["has_all_required_fields"]

        except Exception as e:
            print(f"  ❌ Error: {e}")
            test_result["error"] = str(e)
            results["error_analysis"]["parsing_errors"] += 1

        results["detailed_results"].append(test_result)
        print(f"  ✓ Completed in {test_result.get('extraction_time', 0):.2f}s\n")

    # Calculate aggregate metrics
    if results["accuracy_scores"]:
        results["mean_accuracy"] = sum(results["accuracy_scores"]) / len(results["accuracy_scores"])
    else:
        results["mean_accuracy"] = None

    successful_tests = sum(1 for r in results["detailed_results"] if r["success"])
    results["success_rate"] = successful_tests / len(test_suite)

    return results


def print_evaluation_summary(evaluation_results: Dict):
    """
    Print a formatted summary of evaluation results

    Args:
        evaluation_results (dict): Results from full_evaluation()
    """
    print("\n" + "=" * 60)
    print("EVALUATION SUMMARY")
    print("=" * 60)

    # Success metrics
    print(f"\n📊 Overall Performance:")
    print(f"  Success Rate: {evaluation_results['success_rate']:.1%}")
    if evaluation_results['mean_accuracy'] is not None:
        print(f"  Mean Accuracy: {evaluation_results['mean_accuracy']:.1%}")

    # Error analysis
    print(f"\n❌ Error Analysis:")
    ea = evaluation_results['error_analysis']
    print(f"  Total Tests: {ea['total_tests']}")
    print(f"  Parsing Errors: {ea['parsing_errors']}")
    print(f"  Missing Fields: {ea['missing_fields']}")
    print(f"  Incorrect Values: {ea['incorrect_values']}")

    # Individual test results
    print(f"\n📋 Individual Test Results:")
    for result in evaluation_results['detailed_results']:
        status = "✓" if result['success'] else "✗"
        time_str = f"{result.get('extraction_time', 0):.2f}s"
        acc_str = ""
        if result['accuracy']:
            acc_str = f" - Accuracy: {result['accuracy']['overall_accuracy']:.1%}"
        print(f"  {status} {result['name']}: {time_str}{acc_str}")

    print("\n" + "=" * 60 + "\n")


# ============================================================================
# EXAMPLE USAGE AND TEST SUITE
# ============================================================================

if __name__ == "__main__":
    # Example 1: Basic extraction (original functionality)
    print("Example 1: Basic Extraction")
    print("-" * 60)
    file_url = "https://images.drlogy.com/assets/uploads/lab/pdf/CBC-test-report-format-example-sample-template-Drlogy-lab-report.pdf"
    start_time = time.time()
    result = get_data("lab_report", file_url)
    end_time = time.time()

    print(json.dumps(result, indent=2))
    dur = int(end_time - start_time)
    minutes, seconds = divmod(dur, 60)
    print(f"\nExtraction lasted for {minutes:02d} min {seconds:02d} sec\n")

    # Example 2: Validation of output
    print("\nExample 2: Output Validation")
    print("-" * 60)
    validation = validate_llm_output(result)
    print(json.dumps(validation, indent=2))

    # Example 3: Full evaluation with test suite
    print("\n\nExample 3: Full Evaluation Suite")
    print("-" * 60)

    # Define test suite with ground truth
    test_suite = [
        {
            "name": "cbc_test_report",
            "url": "https://images.drlogy.com/assets/uploads/lab/pdf/CBC-test-report-format-example-sample-template-Drlogy-lab-report.pdf",
            # Ground truth would go here if you know the correct values
            # "ground_truth": {
            #     "patient_name": "John Doe",
            #     "date_of_birth": "1990-01-01",
            #     ...
            # }
        },
        # Add more test cases here
        # {
        #     "name": "test2",
        #     "url": "...",
        # }
    ]

    # Run full evaluation
    evaluation_results = full_evaluation(test_suite)

    # Print summary
    print_evaluation_summary(evaluation_results)

    # Optionally save detailed results to file
    with open("evaluation_results.json", "w") as f:
        json.dump(evaluation_results, f, indent=2)
    print("📁 Detailed results saved to: evaluation_results.json")