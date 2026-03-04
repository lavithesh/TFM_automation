from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://trulyfreehome.dev/")

    driver.implicitly_wait(10)

    print("Website opened successfully")

    return driver