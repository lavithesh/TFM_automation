from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    cart_icon = (By.CSS_SELECTOR,".cart-icon")

    checkout_btn = (By.XPATH,"//button[contains(text(),'Checkout')]")

    def open_cart(self):

        self.click(self.cart_icon)

    def checkout(self):

        self.click(self.checkout_btn)