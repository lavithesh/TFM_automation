from utils.driver_setup import get_driver
from pages.signup_page import SignupPage
from pages.otp_page import OTPPage


def test_end_to_end():

    driver = get_driver()

    print("Page Title:", driver.title)

    signup = SignupPage(driver)
    signup.signup("9895866448")

    otp = OTPPage(driver)
    otp.enter_otp("1111")

    driver.quit()