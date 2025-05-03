import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException

class TestRemove:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
    
    def teardown_method(self, method):
        self.driver.quit()
    
    def find_element_with_retry(self, by, value, timeout=10):
        """Attempts to find an element with retries to handle stale or not found exceptions."""
        wait = WebDriverWait(self.driver, timeout)
        for _ in range(3):  # Retry up to 3 times
            try:
                element = wait.until(EC.presence_of_element_located((by, value)))
                return element
            except (StaleElementReferenceException, NoSuchElementException):
                continue
        raise NoSuchElementException(f"Element with locator ({by}, {value}) not found")

    def test_remove(self):
        try:
            # Step 1: Open the website
            self.driver.get("http://localhost:5173/")
            # Step 2: Set the window size
            self.driver.set_window_size(1552, 832)

            # Step 3: Click on the navigation icon
            nav_icon = self.find_element_with_retry(By.ID, "nav-icon")
            nav_icon.click()

            # Step 4: Click on the CART link
            cart_link = self.find_element_with_retry(By.LINK_TEXT, "CART")
            cart_link.click()

            # Step 5: Click on the remove button
            remove_button = self.find_element_with_retry(By.CSS_SELECTOR, ".remove")
            remove_button.click()

            # Step 6: Wait for and handle the confirmation alert
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            assert alert.text == "Are you sure you want to remove all items?"
            alert.accept()

        except TimeoutException:
            pytest.fail("Timed out waiting for a page element or alert.")
        except NoSuchElementException as e:
            pytest.fail(f"Element not found: {e}")
        except StaleElementReferenceException:
            pytest.fail("Stale element reference exception occurred.")
