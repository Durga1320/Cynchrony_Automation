import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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


@pytest.fixture()
def student_login(intiallizing):
    driver = intiallizing
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    driver.find_element(By.XPATH, "(//div/div[@class='font-medium text-purple-700' ])[1]").click()
    # wait = WebDriverWait(self.driver, 5)
    #wait.until(expected_conditions.presence_of_element_located(self.google_sign_in))
    driver.find_element(By.XPATH, "//div[@class='cl-internal-16pk7q8']/span").click()
    driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("businessidea1320@gmail.com")
    driver.find_element(By.XPATH, "//div[@class='TNTaPb']/div/div/button").click()
   # time.sleep(5)
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@autocomplete='current-password']")))
    driver.find_element(By.XPATH, "//input[@autocomplete='current-password']").send_keys("Jamesdurga@12")

    driver.find_element(By.XPATH, "//div[@class='TNTaPb']/div/div/button").click()

    driver.find_element(By.XPATH, "//div[@class='O1Slxf']/div/div[2]").click()

    wait = WebDriverWait(driver, 30)
    cynchrony_logo = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[text()='Cynchrony']")))

    assert "Cynchrony" == cynchrony_logo.text
    print(cynchrony_logo.text)


