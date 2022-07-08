import unittest
from selenium import webdriver
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.pages.HomePage import HomePage
from src.pages.ResultsPage import ResultsPage


class TestMoreSearchResults(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_more_results(self):
        # Given
        driver = self.driver
        driver.get("https://duckduckgo.com/")

        # When
        home_page = HomePage(driver)
        home_page.search_query("Hello World!\n")

        # And
        results_page = ResultsPage(driver)
        results_page.more_results_button.click()

        # Then
        self.assertIn("2", results_page.page_number_label.text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
