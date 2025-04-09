import pytest
import time
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



@pytest.mark.usefixtures("intiallizing")
class ATS:
    def __init__(self, driver):
        self.driver = driver

        self.login_button = (By.XPATH, "//button[text()='Login']")
        self.student_login_button = (By.XPATH, "(//div/div[@class='font-medium text-purple-700' ])[1]")
        self.google_sign_in = (By.XPATH, "//div[@class='cl-internal-16pk7q8']/span")
        self.email = (By.CSS_SELECTOR, "input[type='email']")
        self.email_sign_button = (By.XPATH, "//div[@class='TNTaPb']/div/div/button")
        self.password = (By.XPATH, "//input[@autocomplete='current-password']")
        self.password_button = (By.XPATH, "//div[@class='TNTaPb']/div/div/button")
        self.continue_button = (By.XPATH, "//div[@class='O1Slxf']/div/div[2]")
        self.logo_visible = (By.XPATH, "//span[text()='Cynchrony']")
        #self.accept_button = (By.ID, 'acceppt-button-content')
        self.Ats_start_button = (By.XPATH, "((//div[@class='p-6'])[1]/div[2]/div/div/a/button[text()='Get Started'])[1]")
        self.resume_upload = (By.XPATH, "//input[@type='file']")
        self.upload_button = (By.XPATH, "//button[normalize-space()='Analyze Resume']")
        self.ats_score = (By.CSS_SELECTOR,"div[class='lg:w-2/3']/div/div[2]/h2")
        self.ats_overall_S= (By.XPATH,"//div[@class='lg:w-2/3']/div/div[2]/div/div/p")
        self.ats_allscores =(By.XPATH,"//div[@class='relative']")


    def test_student_login(self,email,password):

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

        wait = WebDriverWait(self.driver, 30)
        cynchrony_logo = wait.until(expected_conditions.presence_of_element_located(self.logo_visible))

        assert "Cynchrony" == cynchrony_logo.text
        print(cynchrony_logo.text)
       # time.sleep(15)


    def test_ats_analysis(self,filepath):

       self.driver.find_element(*self.Ats_start_button).click()
       resume = self.driver.find_element(*self.resume_upload)
       resume.send_keys(filepath)
       self.driver.find_element(*self.upload_button).click()
       Wait = WebDriverWait(self.driver,10)
       Wait.until(expected_conditions.visibility_of_element_located(self.ats_score))
       ats_Discription =self.driver.find_element(*self.ats_score).text
       overall_score_d=self.driver.find_element(*self.ats_overall_S).text
       ats_all_s = self.driver.find_elements(*self.ats_allscores)
       print(len(ats_all_s))
       for scores in ats_all_s:
           atsscores = scores.find_element(By.XPATH,"div/div").text
           print(atsscores)
       print(f"{ats_Discription}\n{overall_score_d}" )



@pytest.mark.parametrize("email,password,filepath", [
    ("businessidea1320@gmail.com","Jamesdurga@12","F:\\My Resume\\Automation_sel_py.pdf" ),
   # ("durgaprasadkatakamsetti13@gmail.com", "Prasad$12","F:\\My Resume\\Automation_sel_py.pdf"),
    #("anirudhchandana27@gmail.com","Anirudh@2025","F:\\My Resume\\Automation_resume_1.pdf" )
    ])
def test_login_and_analysis(intiallizing,email,password,filepath):
    ats_instance = ATS(intiallizing)
    ats_instance.test_student_login(email,password)
    ats_instance.test_ats_analysis(filepath)





