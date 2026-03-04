from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignupPage(BasePage):

    profile_icon = (By.XPATH, "//a[contains(@class,'user')]")
    create_account_btn = (By.XPATH, "//button[contains(text(),'CREATE ACCOUNT')]")
    phone_input = (By.XPATH, "//input[contains(@placeholder,'Mobile')]")
    continue_btn = (By.XPATH, "//button[contains(text(),'CONTINUE')]")

    def signup(self, phone):

        self.click(self.profile_icon)

        self.click(self.create_account_btn)

        self.type(self.phone_input, phone)

        self.click(self.continue_btn)