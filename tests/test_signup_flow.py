from utils.driver_setup import get_driver
from pages.signup_page import SignupPage


def test_end_to_end():

    driver = get_driver()

    print("Page Title:", driver.title)

    signup = SignupPage(driver)

    signup.signup("9895866448")

    driver.quit()