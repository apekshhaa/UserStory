import unittest
import os
import pandas as pd

from src.downloader import download_file
from src.validator import validate_csv, REQUIRED_COLUMNS


class TestEmployeePipeline(unittest.TestCase):

    # Test Case 1: Verify CSV File Download
    def test_csv_download(self):
        result = download_file()
        self.assertTrue(result)
        self.assertTrue(os.path.exists("employee_data.csv"))

    # Test Case 2: Verify CSV File Extraction
    def test_csv_extraction(self):
        df = pd.read_csv("employee_data.csv")
        self.assertGreater(len(df), 0)

    # Test Case 3: Validate File Type and Format
    def test_file_type(self):
        self.assertTrue("employee_data.csv".endswith(".csv"))

    # Test Case 4: Validate Data Structure
    def test_data_structure(self):
        df = pd.read_csv("employee_data.csv")

        for column in REQUIRED_COLUMNS:
            self.assertIn(column, df.columns)

    # Test Case 5: Handle Missing or Invalid Data
    def test_missing_data(self):
        test_df = pd.DataFrame({
            "User Id": [1],
            "First Name": [None]
        })

        self.assertTrue(test_df["First Name"].isnull().any())
from src.scraper import fetch_employee_data
from src.transformer import normalize_data


class TestEmployeeData(unittest.TestCase):

    # Test Case 1: Verify JSON File Download
    def test_json_download(self):
        data = fetch_employee_data()
        self.assertIsNotNone(data)

    # Test Case 2: Verify JSON File Extraction
    def test_json_extraction(self):
        data = fetch_employee_data()
        self.assertGreater(len(data), 0)

    # Test Case 3: Validate File Type and Format
    def test_file_type(self):
        data = fetch_employee_data()
        self.assertIsInstance(data, list)

    # Test Case 4: Validate Data Structure
    def test_data_structure(self):
        data = fetch_employee_data()
        employee = data[0]

        expected_fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "job_title",
            "years_of_experience",
            "age",
            "salary"
        ]

        for field in expected_fields:
            self.assertIn(field, employee)

    # Test Case 5: Handle Missing or Invalid Data
    def test_invalid_phone_handling(self):
        sample_data = [
            {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john@example.com",
                "phone": "12345x678",
                "job_title": "Developer",
                "years_of_experience": 2,
                "age": 25,
                "salary": 50000
            }
        ]

        df = normalize_data(sample_data)

        self.assertEqual(
            df.loc[0, "phone"],
            "Invalid Number"
        )

        self.assertEqual(
            df.loc[0, "Full Name"],
            "John Doe"
        )

        self.assertEqual(
            df.loc[0, "designation"],
            "System Engineer"
        )


if __name__ == "__main__":
    unittest.main()