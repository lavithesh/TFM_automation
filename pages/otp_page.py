from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class OTPPage(BasePage):

    otp_input = (By.XPATH, "//input[@type='tel']")
    verify_btn = (By.XPATH, "//button[contains(.,'Verify') or contains(.,'VERIFY')]")

    # phone field from previous page
    phone_input = (By.XPATH, "//input[@placeholder='Mobile number*']")

    def enter_otp(self, otp):

        wait = WebDriverWait(self.driver, 30)

        print("Step 6: Waiting for OTP page")

        # wait until phone input disappears (means OTP page loaded)
        wait.until(
            EC.invisibility_of_element_located(self.phone_input)
        )

        print("OTP page loaded")

        # wait for OTP field
        otp_field = wait.until(
            EC.visibility_of_element_located(self.otp_input)
        )

        print("Step 7: Enter OTP")

        otp_field.clear()
        otp_field.send_keys(otp)

        print("OTP entered")

        # click verify
        verify_button = wait.until(
            EC.element_to_be_clickable(self.verify_btn)
        )

        verify_button.click()

        print("OTP verified successfully")