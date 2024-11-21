# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # service = Service("/Users/virupaksha/PycharmProjects/python_selenium_minicourse/chromedriver.exe")
# # driver = webdriver.Chrome(service=service)
# # driver.get("https://www.amazon.com")
# # breakpoint()
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
# driver.get("https://www.amazon.com")
# search=driver.find_element(By.ID,'twotabsearchtextbox')
# search.send_keys('dress',Keys.ENTER)
# search_bar = driver.find_element(By.NAME,"field-keywords")
#
# search_bar.send_keys("dress")
#
# search_bar.send_keys(Keys.RETURN)
# breakpoint()
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestAmazon:
    search_words=('dress','shoes','toys')
    driver = ''
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.amazon.com")

    @pytest.mark.parametrize('search_query',search_words)

    def test_amazon_search_dress(self,search_query):
        # driver = webdriver.Firefox()
        # driver.implicitly_wait(5)
        # driver.get("https://www.amazon.com")
        search = self.driver.find_element(By.NAME, "field-keywords")
        search.send_keys(search_query)
        search.send_keys(Keys.RETURN)
        time.sleep(5)
        expected_text= f'\"{search_query}\"'
        actual_text=self.driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text
        assert expected_text == actual_text,f'Error, Expected text {expected_text}, but actual text: {actual_text}'

    def teardown_method(self):
        self.driver.quit()






