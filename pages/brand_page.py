from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BrandPage(BasePage):

    menu_btn = (By.XPATH, "//button[contains(@class,'menu')]")

    brands_btn = (By.XPATH, "//a[contains(text(),'Brands')]")

    def open_brand_page(self):

        print("Opening menu")

        self.click(self.menu_btn)

        print("Opening brands")

        self.click(self.brands_btn)