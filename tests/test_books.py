import unittest
import os
import pandas as pd
import sys

sys.path.append("src")

from scraper import scrape_page


class TestBookScraper(unittest.TestCase):

    def setUp(self):
        self.url = "http://books.toscrape.com/"
        self.books = scrape_page(self.url)

    # Test Case 1
    def test_scraper_download(self):
        self.assertGreater(len(self.books), 0)
        print("Test 1 Passed: Book data downloaded successfully")

    # Test Case 2
    def test_csv_extraction(self):
        df = pd.DataFrame(self.books)
        df.to_csv("test_books.csv", index=False)

        self.assertTrue(os.path.exists("test_books.csv"))
        print("Test 2 Passed: CSV file created successfully")

    # Test Case 3
    def test_file_type(self):
        filename = "test_books.csv"
        self.assertTrue(filename.endswith(".csv"))
        print("Test 3 Passed: File type is valid CSV")

    # Test Case 4
    def test_data_structure(self):
        expected_columns = ["Title", "Price", "Rating", "Availability", "URL"]
        df = pd.DataFrame(self.books)

        self.assertEqual(list(df.columns), expected_columns)
        print("Test 4 Passed: Data structure is correct")

    # Test Case 5
    def test_missing_data(self):
        df = pd.DataFrame(self.books)
        self.assertFalse(df.isnull().values.any())
        print("Test 5 Passed: No missing or invalid data")


if __name__ == "__main__":
    unittest.main()