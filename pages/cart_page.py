from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    cart_icon = (By.XPATH, "//a[contains(@href,'cart')]")

    checkout_btn = (By.XPATH, "//button[contains(text(),'Checkout')]")

    def open_cart(self):

        print("Opening cart")

        self.click(self.cart_icon)

    def checkout(self):

        print("Proceeding to checkout")

        self.click(self.checkout_btn)