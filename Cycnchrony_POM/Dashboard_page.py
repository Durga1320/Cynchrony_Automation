import time

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Dashboard_Page:

    def __init__(self, driver):
        self.driver =  driver
        self.student_name =(By.XPATH,"//div[@class='relative z-10']/div/h1")
        self.Ats_start_button =(By.XPATH,"((//div[@class='p-6'])[1]/div[2]/div/div/a/button[text()='Get Started'])[1]")
        self.resume_upload= (By.XPATH,"//input[@type='file']")
        self.upload_button =(By.XPATH, "//button[text()='Analyze Resume']")




    def student_Dashboard(self):
        # verifying student_name
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.visibility_of_element_located(self.student_name))
        s_name=self.driver.find_element(*self.student_name)
        #assert "Hi Durgaprasad !" == s_name.text
        print(s_name.text)

    def ATS_Analysis(self):

        filepath ="F:\\My Resume\\Automation_resume_1.pdf"
        self.driver.find_element(*self.Ats_start_button).click()
        resume=self.driver.find_element(*self.resume_upload)
        resume.send_keys(filepath)
        self.driver.find_element(*self.upload_button).click()

        time.sleep(15)

