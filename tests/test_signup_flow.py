from utils.driver_setup import get_driver
from pages.signup_page import SignupPage
from pages.brand_page import BrandPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_end_to_end():

    driver = get_driver()

    print("Page Title:", driver.title)

    signup = SignupPage(driver)
    brand = BrandPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    signup.signup("9895866448")

    brand.open_brand_page()

    product.select_product()

    product.add_product_to_cart()

    cart.open_cart()

    cart.checkout()

    driver.quit()