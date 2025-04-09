
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Cycnchrony_POM.Dashboard_page import Dashboard_Page


class Login_Page:

    def __init__(self,driver):
        self.driver=driver
        self.login_button = (By.XPATH,"//button[text()='Login']")
        self.student_login_button =(By.XPATH, "(//div/div[@class='font-medium text-purple-700' ])[1]")
        self.google_sign_in =(By.XPATH, "//div[@class='cl-internal-16pk7q8']/span")
        self.email = (By.CSS_SELECTOR,"input[type='email']")
        self.email_sign_button=(By.XPATH, "//div[@class='TNTaPb']/div/div/button")
        self.password =(By.XPATH,"//input[@autocomplete='current-password']")
        self.password_button=(By.XPATH, "//div[@class='TNTaPb']/div/div/button")
        self.continue_button =(By.XPATH,"//div[@class='O1Slxf']/div/div[2]")
        self.logo_visible= (By.XPATH,"//span[text()='Cynchrony']")



    def student_login(self):
        email = "businessidea1320@gmail.com"
        password = "Jamesdurga@12"
        self.driver.find_element(*self.login_button).click()
        self.driver.find_element(*self.student_login_button).click()
       # wait = WebDriverWait(self.driver, 5)
        #wait.until(expected_conditions.presence_of_element_located(self.google_sign_in))
        self.driver.find_element(*self.google_sign_in).click()
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.email_sign_button).click()
        time.sleep(5)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.password))
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.password_button).click()
        self.driver.find_element(*self.continue_button).click()
        wait = WebDriverWait(self.driver, 10)
        cynchrony_logo = wait.until(expected_conditions.presence_of_element_located(self.logo_visible))

        assert "Cynchrony" == cynchrony_logo.text
        print(cynchrony_logo.text)
        Dashboardpage = Dashboard_Page(self.driver)
        return Dashboardpage









