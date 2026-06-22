import unittest
import os

from src.downloader import download_zip
from src.extractor import extract_zip
from src.validator import validate_excel


class TestEmployeePipeline(unittest.TestCase):

    # Test Case 1
    def test_zip_download(self):
        result = download_zip()
        self.assertTrue(result)
        self.assertTrue(os.path.exists("employee_data.zip"))

    # Test Case 2
    def test_excel_extraction(self):
        download_zip()
        excel_file = extract_zip()

        self.assertIsNotNone(excel_file)
        self.assertTrue(os.path.exists(excel_file))

    # Test Case 3
    def test_file_type(self):
        download_zip()
        excel_file = extract_zip()

        self.assertTrue(
            excel_file.endswith(".xlsx")
            or excel_file.endswith(".xls")
        )

    # Test Case 4
    def test_data_structure(self):
        download_zip()
        excel_file = extract_zip()

        self.assertTrue(validate_excel(excel_file))

    # Test Case 5
    def test_invalid_file(self):
        self.assertFalse(
            validate_excel("fake_file.xlsx")
        )


if __name__ == "__main__":
    unittest.main()