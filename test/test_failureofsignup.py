import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestFailureOfSignup:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1552, 832)
    
    def teardown_method(self, method):
        self.driver.quit()
    
    def test_failureofsignup(self):
        self.driver.get("http://localhost:5173/")
        
        # Open the navigation menu
        nav_icon = self.driver.find_element(By.ID, "nav-icon")
        actions = ActionChains(self.driver)
        actions.click_and_hold(nav_icon).perform()
        actions.release(nav_icon).perform()

        # Navigate to the signup page
        self.driver.find_element(By.LINK_TEXT, "LOGIN").click()
        self.driver.find_element(By.LINK_TEXT, "Signup").click()

        # Fill in the signup form
        self.driver.find_element(By.ID, "uname").send_keys("KrishnaYadav")
        self.driver.find_element(By.ID, "email").send_keys("krishna.y1808@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("ky123456")
        self.driver.find_element(By.ID, "confirm-password").send_keys("ky123456")
        self.driver.find_element(By.CSS_SELECTOR, ".button").click()

        # Simulate failure of signup by changing input data
        uname_field = self.driver.find_element(By.ID, "uname")
        uname_field.clear()
        uname_field.send_keys("KY123")

        email_field = self.driver.find_element(By.ID, "email")
        email_field.clear()
        email_field.send_keys("krishna123@gmail.com")

        self.driver.find_element(By.CSS_SELECTOR, ".button").click()

        # Verify if the alert with expected text appears
        try:
            WebDriverWait(self.driver, 15).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            assert alert.text == "User signed up"
            alert.accept()
        except TimeoutException:
            print("Alert not found within the timeout period.")
            self.driver.save_screenshot("debug_screenshot.png")
            raise
