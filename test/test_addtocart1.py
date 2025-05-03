import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

class TestAddToCart():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)  # Explicit wait

    def teardown_method(self, method):
        self.driver.quit()

    def test_add_to_cart(self):
        # Open the webpage
        self.driver.get("http://localhost:5173/")
        # Set the window size
        self.driver.set_window_size(1552, 832)

        # Click on the collections link
        collections_selector = ".nav-text:nth-child(2) > .collections"
        collections_element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, collections_selector)))
        collections_element.click()

        # Mouse over the collections link
        actions = ActionChains(self.driver)
        collections_element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, collections_selector)))
        actions.move_to_element(collections_element).perform()


        

       
