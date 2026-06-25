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

    # Test Case 1: Verify CSV File Download
    def test_scraper_download(self):
        self.assertGreater(len(self.books), 0)

    # Test Case 2: Verify CSV File Extraction
    def test_csv_extraction(self):
        df = pd.DataFrame(self.books)
        df.to_csv("test_books.csv", index=False)

        self.assertTrue(os.path.exists("test_books.csv"))

    # Test Case 3: Validate File Type and Format
    def test_file_type(self):
        filename = "test_books.csv"
        self.assertTrue(filename.endswith(".csv"))

    # Test Case 4: Validate Data Structure
    def test_data_structure(self):
        expected_columns = ["Title", "Price", "Rating", "Availability", "URL"]
        df = pd.DataFrame(self.books)

        self.assertEqual(list(df.columns), expected_columns)

    # Test Case 5: Handle Missing or Invalid Data
    def test_missing_data(self):
        df = pd.DataFrame(self.books)
        self.assertFalse(df.isnull().values.any())


if __name__ == "__main__":
    unittest.main()