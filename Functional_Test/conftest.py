import pytest
from selenium import webdriver


@pytest.fixture()
def intiallizing():

    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    driver.get("https://cynchrony.in/")
   # driver.minimize_window()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


