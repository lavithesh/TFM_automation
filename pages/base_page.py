from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):

        print("Trying to click:", locator)

        element = WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable(locator)
        )

        element.click()

        print("Click successful")

    def type(self, locator, text):

        print("Typing:", text)

        element = WebDriverWait(self.driver,20).until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()
        element.send_keys(text)

        print("Typing successful")