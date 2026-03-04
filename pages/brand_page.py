from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BrandPage(BasePage):

    menu_btn = (By.XPATH,"//button[@aria-label='menu']")
    brands_btn = (By.XPATH,"//a[contains(text(),'Brands')]")

    def open_brand_page(self):

        self.click(self.menu_btn)

        self.click(self.brands_btn)