from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class SignupPage(BasePage):

    # Locators
    profile_icon = (By.XPATH, "//*[@data-testid='login-account']")
    create_account_btn = (By.XPATH, "//button[contains(.,'Create')]")

    country_dropdown = (By.CSS_SELECTOR, ".selected-flag")
    india_option = (By.XPATH, "//li[@data-country-code='in']")

    phone_input = (By.XPATH, "//input[contains(@placeholder,'Mobile')]")

    continue_btn = (By.XPATH, "//button[contains(.,'CONTINUE')]")

    def signup(self, phone):

        wait = WebDriverWait(self.driver, 20)

        print("Step 1: Click profile icon")
        wait.until(EC.element_to_be_clickable(self.profile_icon)).click()

        print("Step 2: Click create account")
        wait.until(EC.element_to_be_clickable(self.create_account_btn)).click()

        print("Step 3: Select country +91")

        wait.until(EC.element_to_be_clickable(self.country_dropdown)).click()
        wait.until(EC.element_to_be_clickable(self.india_option)).click()

        print("India selected")

        print("Step 4: Enter phone number")

        phone_field = wait.until(
            EC.element_to_be_clickable(self.phone_input)
        )

        phone_field.click()
        time.sleep(1)

        phone_field.clear()
        time.sleep(1)

        # Type slowly so React input accepts digits
        for digit in phone:
            phone_field.send_keys(digit)
            time.sleep(0.3)

        print("Phone number entered")
        print("Actual value:", phone_field.get_attribute("value"))

        print("Step 5: Click Continue")

        wait.until(
            EC.element_to_be_clickable(self.continue_btn)
        ).click()

        print("Continue clicked successfully")