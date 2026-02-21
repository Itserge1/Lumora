import pytest
from llm_data_extraction import get_data
from validation_tests import (
    is_valid_json
)


class TestLLMDataExtraction:
    file_data = [
        ("lab_report", "https://images.drlogy.com/assets/uploads/lab/pdf/CBC-test-report-format-example-sample-template-Drlogy-lab-report.pdf")
    ]

    @pytest.mark.parametrize("file_name,file_url", file_data)
    def test_isvalid_json_output(self, file_name, file_url):
        output_data = get_data(file_name, file_url)
        assert is_valid_json(output_data), f"Invalid JSON output for {file_url}"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
