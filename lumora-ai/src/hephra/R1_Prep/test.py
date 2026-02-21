from typing import Dict, List
from llm_data_extraction import get_data

def evaluate_extraction_structural_format(ground_truth:Dict, output_data:Dict) -> Dict:
    metrics = {
        "missing_fields": [],
        "extra_fields": [],
        "present_field":{},
        "structural_accuracy": 0.0,
        "lab_tests_infos": {
            "valid_test": 0,
            "bad_test": [],
            "error": "",
            "structural_accuracy":0.0
        },
    }

    # Get all missing field
    for field in ground_truth.keys():
        if field not in output_data.keys():
            metrics["missing_fields"].append(field)
            metrics["present_field"][field] = False
        else:
            metrics["present_field"][field] = True

    # Get all extra field
    for field in output_data.keys():
        if field not in ground_truth.keys():
            metrics["extra_fields"].append(field)

    # Compute percentage of structural accuracy
    expected_fields = len(ground_truth.keys())
    total_present_fields =  sum(1 for present in metrics["present_field"].values() if present)
    if expected_fields > 0:
        metrics["structural_accuracy"] = total_present_fields / expected_fields

    # GET LAB TEST METRICS
    lab_tests_arr = output_data["lab_tests"]
    expected_lab_test_field = set(ground_truth["lab_tests"][0].keys())

    if isinstance(lab_tests_arr, List):
        for idx,test in enumerate(lab_tests_arr):
            if isinstance(test, Dict):
                test_field = set(test.keys())

                # missing field
                missing = expected_lab_test_field - test_field

                # extra field
                extra = test_field - expected_lab_test_field

                if not missing and not extra:
                    metrics["lab_tests_infos"]["valid_test"] += 1
                else:
                    metrics["lab_tests_infos"]["bad_test"].append({
                        "idx": idx,
                        "missing": list(missing),
                        "extra": list(extra),
                    })
            else:
                metrics["lab_tests_infos"]["bad_test"].append({
                    "id":idx,
                    "test":test,
                    "error": f"lab text at id {idx} is not a valid object"
                })

    else:
        metrics["lab_tests_infos"]["error"] = "lab_test id not a valid list"

    # COMPUTE LAB_TESTS STRUCTURAL ACCURACY PERCENTAGE
    metrics["lab_tests_infos"]["structural_accuracy"] = metrics["lab_tests_infos"]["valid_test"] / len(lab_tests_arr)

    return metrics


if __name__ == "__main__":
    file_name = "lab_report"
    file_url = "https://images.drlogy.com/assets/uploads/lab/pdf/CBC-test-report-format-example-sample-template-Drlogy-lab-report.pdf"

    predicted = get_data(file_name, file_url)
    ground_truth = {
        "patient_name": "Yash M. Patel",
        "date_of_birth": None,
        "report_date": "2022-12-02",
        "ordering_physician": "Dr. Hiren Shah",
        "lab_tests": [
            {
                "test_name": "Hemoglobin (Hb)",
                "value": 12.5,
                "status": "Low",
                "reference_value": "13.0 - 17.0",
                "unit": "g/dL"
            }
        ]
    }

    metrics = evaluate_extraction_structural_format(ground_truth, predicted)
    print(metrics)
