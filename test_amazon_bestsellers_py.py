import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestAmazon:
    driver = ''

    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.amazon.com/")

    def test_empty_method(self):
        # Click on the "Today's Deals" link (example, as bestsellers isn't direct in the navbar)
        self.driver.find_element(By.XPATH, "//div[@id='nav-xshop']//a[contains(@href,'goldbox')]").click()

        # Wait for the page to load
        time.sleep(5)

        # Find all links within the sub-navigation bar
        actual_links = self.driver.find_elements(By.XPATH, "//div[@id='nav-subnav']//a")

        # Assert that there are 5 links (or any expected number of links)
        assert len(actual_links) == 6, f'Expected to see 6 bestseller links, but got {len(actual_links)}'

    def teardown_method(self):
        self.driver.quit()
