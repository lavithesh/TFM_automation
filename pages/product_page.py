from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):

    first_product = (By.XPATH, "(//div[contains(@class,'product')])[1]")

    add_to_cart = (By.XPATH, "//button[contains(text(),'Add to Cart')]")

    def select_product(self):

        print("Selecting first product")

        self.click(self.first_product)

    def add_product_to_cart(self):

        print("Adding product to cart")

        self.click(self.add_to_cart)