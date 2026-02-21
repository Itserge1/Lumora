import os
import io
import time
import json
import base64
import requests
import pdfplumber
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# Load all env
load_dotenv()

# Create Client
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Download Bytes from online pdf
def download_pdf_bytes(file_url):
  response = requests.get(file_url)
  response.raise_for_status()
  return response.content

# Extract Text from pdf
def get_text_from_pdf(file_url):
  pdf_bytes = download_pdf_bytes(file_url)
  with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf_file:
    pdf_text = "\n".join([page.extract_text() for page in pdf_file.pages])
  return pdf_text

# Save output in a json file
def save_data_in_json_file(file_name, data):
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving data to {file_name}: {e}")
        raise

def get_pdf_bytes_local_file(file_name):
    file_path = Path(__file__).parent / "data" / "pdf" / "medical_lab_reports"/ f"{file_name}.pdf"

    with open(file_path, "rb") as f:
        file_bytes = f.read()

    pdf_base64 = base64.b64encode(file_bytes).decode("utf-8")
    return pdf_base64

# Encode Pdf Bytes in base64
def get_pdf_base64(file_url):
  pdf_bytes = download_pdf_bytes(file_url)
  pdf_base64 = base64.b64encode(pdf_bytes).decode("utf-8")
  return pdf_base64

def get_data(file_name, file_url):
  # get pdf bytes and encode it in base64 online
  # base64_pdf = get_pdf_base64(file_url)

  # get pdf bytes and encode it in base64 local
  base64_pdf = get_pdf_bytes_local_file(file_name)

  # # get text from pdf
  # pdf_text = get_text_from_pdf(file_url)

  # prepare my prompt
  my_prompt = f"""
  You are a medical data extraction software.
  Extract the data from the provided pdf file or text
  Return the output in JSON

  RULES:
  - Only output a valid JSON
  - Do not provide any commentary or markdowns
  - If a field do not exist, set it to null
  - Dates must be in YYYY-MM-DD format
  - If multiple patients exist, extract only the first one
  - extract all the test and store it in the lab_tests array 
  - If extraction fails, return a JSON  with an "error" key an the reason as value of that key

  JSON FORMAT:
  {{
    "patient_name": "string or null",
    "date_of_birth": "YYYY-MM-DD or null",
    "report_date": "YYYY-MM-DD or null",
    "ordering_physician": "string or null",
    "lab_tests": [
      {{
        "test_name":"string or null",
        "value":"float or null",
        "status":"string or null",
        "reference_value":"string or null",
        "unit":"string or null",
      }}
    ]
  }}
  """

  print(f"Extraction for {file_name}.pdf in progress...")

  # prepare my response base64
  response = client.responses.create(
    model="gpt-4o-mini",
    temperature=0,
    input=[
      {
        "role":"user",
        "content": [
          {
            "type": "input_file",
            "filename": f"{file_name}.pdf",
            "file_data": f"data:application/pdf;base64, {base64_pdf}",
          },
          {
            "type": "input_text",
            "text": my_prompt,
          }
        ]
      }
    ]
  )
  data = json.loads(response.output_text)
  save_data_in_json_file(file_name, data)

  # # prepare my response text
  # response_text_approach = client.chat.completions.create(
  #   model="gpt-4o-mini",
  #   temperature=0,
  #   messages=[{"role":"user", "content":my_prompt}]
  # )
  # data_text_approach = json.loads(response_text_approach.choices[0].message.content)
  # save_data_in_json_file(file_name, data_text_approach)

  return data

if __name__ == "__main__":
  file_url = "https://images.drlogy.com/assets/uploads/lab/pdf/CBC-test-report-format-example-sample-template-Drlogy-lab-report.pdf"
  start_time = time.time()
  get_data("02_report_cbc_with_differential_blood", file_url)
  end_time = time.time()
  dur = int(end_time - start_time)
  minutes, seconds = divmod(dur, 60)
  print(f"Extraction lasted for {minutes:02d} min {seconds:02d} sec")

