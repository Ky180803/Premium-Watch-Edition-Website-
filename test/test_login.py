import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
    
    def teardown_method(self, method):
        self.driver.quit()
    
    def test_login(self):
        # Step 1: Open the website
        self.driver.get("http://localhost:5173/")
        # Step 2: Set the window size
        self.driver.set_window_size(1552, 832)
        
        # Step 3: Wait for the navigation icon and click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav-icon > span:nth-child(1)"))
        ).click()

        # Step 4: Wait for the LOGIN link and click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "LOGIN"))
        ).click()

        # Step 5: Wait for the email field, click, and type the email
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "email"))
        ).send_keys("krishna.y1808@gmail.com")

        # Step 6: Wait for the password field, click, and type the password
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password"))
        ).send_keys("ky123456")

        # Step 7: Wait for the login button and click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button:nth-child(2)"))
        ).click()

        # Optionally: Include any other steps or verifications needed after login

