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
        self.driver.get("https://www.amazon.com")

    def test_empty_method(self):
        self.driver.find_element(By.ID,'nav-cart').click()
        time.sleep(5)
        actual_text=self.driver.find_element(By.XPATH, "//div[@id='sc-active-cart']//h2").text
        expected_text='Your Amazon Cart is empty'
        assert expected_text == actual_text, f'Error, Expected text {expected_text}, but actual text: {actual_text}'

    def teardown_method(self):
        self.driver.quit()