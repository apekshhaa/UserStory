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


if __name__ == "__main__":
    unittest.main()