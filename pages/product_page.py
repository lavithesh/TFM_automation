from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):

    first_product = (By.CSS_SELECTOR,".product-card")

    add_to_cart = (By.XPATH,"//button[contains(text(),'Add to Cart')]")

    def select_product(self):

        self.click(self.first_product)

    def add_product_to_cart(self):

        self.click(self.add_to_cart)