import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("intiallizing","student_login")
class CoverLetter:

    def __init__(self,driver):
        self.driver =driver
        self.career_sync = (By.XPATH, "//ul[@class='space-y-6']/li[2]/button/div")
        self.create_resume_button = (By.CSS_SELECTOR, "ul[class='mt-2 ml-9 space-y-1'] li")
        self.CL_JD =(By.XPATH,"//div[contains(@class,'lg:w-1/3 space-y-4')]/div/textarea")
        self.upload_resume= (By.XPATH,"//input[@type='file']")
        self.generate_CL =(By.XPATH,"(//div[contains(@class,'border border-gray-100')])[2]/button[text()='Generate Cover Letter']")
        self.copy_button =(By.XPATH,"//div[@class='relative']/div/button[1]")
        self.download_button =(By.XPATH,"//div[@class='relative']/div/button[2]")

    def test_cover_letter(self):
        file_path = "F:\\My Resume\\Automation_resume_1.pdf"
        #folder_path = "Screenshorts"

        with open("data/Job_discription.txt", "r", encoding="utf-8") as file:

            long_description = file.read()

        try:
            self.driver.find_element(*self.career_sync).click()
            time.sleep(4)
            list_of_options = self.driver.find_elements(*self.create_resume_button)
            for option in list_of_options:
                if option.text == "Cover Letter Generator":
                    self.C_R = option.find_element(By.CSS_SELECTOR, " a").click()
                    break
            assert element_to_be_clickable(self.C_R)

            cl_jd =self.driver.find_element(*self.CL_JD)
            cl_jd.send_keys(long_description)
            self.driver.find_element(*self.upload_resume).send_keys(file_path)
            #self.driver.execute_script("window.scrollTo(0,300)")
            self.driver.find_element(*self.generate_CL).click()
            wait = WebDriverWait(self.driver,20)
            wait.until(expected_conditions.visibility_of_element_located(self.copy_button))

            self.driver.find_element(*self.copy_button).click()
            self.driver.find_element(*self.download_button).click()
            time.sleep(4)


        except Exception as e:
            print(f"issue in cover_letter: {e}")
            raise

def test_generate_cover_letter(intiallizing,student_login):
    cover_L = CoverLetter(intiallizing)
    cover_L.test_cover_letter()