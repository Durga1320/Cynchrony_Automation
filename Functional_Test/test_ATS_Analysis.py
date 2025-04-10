import pytest
import time
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
        self.password_button = (By.XPATH, "(//div[@class='VfPpkd-dgl2Hf-ppHlrf-sM5MNb']//span[@class='VfPpkd-vQzf8d'])[2]")
        self.continue_button = (By.XPATH, "//div[@class='O1Slxf']/div/div[2]")
        self.logo_visible = (By.XPATH, "//span[text()='Cynchrony']")
        #self.accept_button = (By.ID, 'acceppt-button-content')
        self.Ats_start_button = (By.XPATH, "((//div[@class='p-6'])[1]/div[2]/div/div/a/button[text()='Get Started'])[1]")
        self.resume_upload = (By.XPATH, "//input[@type='file']")
        self.upload_button = (By.XPATH, "(//button[normalize-space()='Analyze Resume'])[1]")
        self.ats_score = (By.XPATH,"//div[@class='lg:w-2/3']/div/div[2]/h2")
        self.over_all_score = (By.XPATH, "(//div[@class='relative']/div/div)[1]")
        self.fomat_score = (By.XPATH,"(//div[@class='relative']/div/div)[2]")
        self.content_score = (By.XPATH, "(//div[@class='relative']/div/div)[3]")
        self.keyword_score = (By.XPATH, "(//div[@class='relative']/div/div)[4]")


    def test_student_login(self,email,password):
        try:

            self.driver.find_element(*self.login_button).click()
            self.driver.find_element(*self.student_login_button).click()
            
            self.driver.find_element(*self.google_sign_in).click()
            self.driver.find_element(*self.email).send_keys(email)
            self.driver.find_element(*self.email_sign_button).click()
            time.sleep(5)
            wait = WebDriverWait(self.driver, 20)
            wait.until(expected_conditions.presence_of_element_located(self.password))
            self.driver.find_element(*self.password).send_keys(password)
            wait = WebDriverWait(self.driver, 10)
            wait.until(expected_conditions.presence_of_element_located(self.password_button))
            self.driver.find_element(*self.password_button).click()

            self.driver.find_element(*self.continue_button).click()

            wait = WebDriverWait(self.driver, 30)
            cynchrony_logo = wait.until(expected_conditions.presence_of_element_located(self.logo_visible))

            assert "Cynchrony" == cynchrony_logo.text
            print(f"Login successful. Logo text: {cynchrony_logo.text}")

        except Exception as e:
            print(f"Login failed: {e}")
            raise

    def test_ats_analysis(self,filepath):
        try:
           wait= WebDriverWait(self.driver,10)
           wait.until(expected_conditions.presence_of_element_located(self.Ats_start_button))
           self.driver.find_element(*self.Ats_start_button).click()
           resume = self.driver.find_element(*self.resume_upload)
           resume.send_keys(filepath)
           analys_button=self.driver.find_element(*self.upload_button)
           analys_button.click()
           Wait = WebDriverWait(self.driver, 20)
           Wait.until(expected_conditions.visibility_of_element_located(self.ats_score))
           ats_Discription =self.driver.find_element(*self.ats_score).text
           Over_All_Score =self.driver.find_element(*self.over_all_score).text
           Format_score = self.driver.find_element(*self.fomat_score).text
           Content_score = self.driver.find_element(*self.content_score).text
           Keyword_score = self.driver.find_element(*self.keyword_score).text
           print(f"{ats_Discription}")
           print(f"overall_score:{Over_All_Score}\nformat_score:{Format_score}\ncontent_score:{Content_score}\nkeyword_score:{Keyword_score}")

        except Exception as e:
            print(f"Login failed: {e}")
            raise



@pytest.mark.parametrize("email,password,filepath", [
    ("businessidea1320@gmail.com","Jamesdurga@12","F:\\My Resume\\Automation_sel_py.pdf" ),
   #("durgaprasadkatakamsetti13@gmail.com", "Prasad$12","F:\\My Resume\\Automation_sel_py.pdf"),
    #("anirudhchandana27@gmail.com","Anirudh@2025","F:\\My Resume\\Automation_resume_1.pdf" )
    ])
def test_login_and_analysis(intiallizing,email,password,filepath):
    ats_instance = ATS(intiallizing)
    ats_instance.test_student_login(email,password)
    ats_instance.test_ats_analysis(filepath)







