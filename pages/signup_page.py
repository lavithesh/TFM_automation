from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SignupPage(BasePage):

    # Profile icon
    profile_icon = (By.XPATH, "//*[@data-testid='login-account']")

    # Create account button
    create_account_btn = (By.XPATH, "//button[contains(text(),'CREATE ACCOUNT')]")

    # Phone number
    phone_input = (By.XPATH, "//input[contains(@placeholder,'Mobile')]")

    # Continue
    continue_btn = (By.XPATH, "//button[contains(text(),'CONTINUE')]")

    def signup(self, phone):

        print("Step 1: Click profile icon")

        self.click(self.profile_icon)

        print("Step 2: Wait for popup")

        WebDriverWait(self.driver,20).until(
            EC.visibility_of_element_located(self.create_account_btn)
        )

        print("Step 3: Click create account")

        self.click(self.create_account_btn)

        print("Step 4: Enter phone number")

        self.type(self.phone_input, phone)

        print("Step 5: Click continue")

        self.click(self.continue_btn)

        print("Signup step finished")