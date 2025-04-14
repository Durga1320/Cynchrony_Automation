import datetime
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("intiallizing","student_login")
class JD_parsing:
    def __init__(self,driver):
        self.driver =driver
        self.career_sync = (By.XPATH, "//ul[@class='space-y-6']/li[2]/button/div")
        self.create_resume_button = (By.CSS_SELECTOR, "ul[class='mt-2 ml-9 space-y-1'] li")
        self.Jd_text =(By.XPATH,"//div[@class='max-w-7xl mx-auto']/h1")
        self.resume_upload = (By.XPATH, "//input[@type='file']")
        self.jd_description =(By.XPATH,"(//div[contains(@class,'border-gray-10')])[2]/textarea")
        self.jd_analyz_button = (By.XPATH,"(//div[@class='lg:w-1/3 space-y-4 md:space-y-6'])/button")
        self.jd_text_visible =(By.XPATH,"//h2[text()='Job Match Score']")
        self.jd_over_all_s =(By.XPATH,"(//div[@class='relative']/div/div[@class='text-4xl font-bold'])[1]")
        self.jd_skills_s =(By.XPATH,"(//div[@class='relative']/div/div[@class='text-4xl font-bold'])[2]")
        self.jd_experience_s =(By.XPATH,"(//div[@class='relative']/div/div[@class='text-4xl font-bold'])[3]")
        self.jd_education_s =(By.XPATH,"(//div[@class='relative']/div/div[@class='text-4xl font-bold'])[4]")



    def test_jd_parsing(self):

        file_path="F:\\My Resume\\Automation_resume_1.pdf"
        folder_path="Screenshorts"

        with open("data/Job_discription.txt", "r", encoding="utf-8") as file:

            long_description = file.read()

        try:
            self.driver.find_element(*self.career_sync).click()
            list_of_options = self.driver.find_elements(*self.create_resume_button)
            for option in list_of_options:
                if option.text == "JD Parsing":
                    self.C_R = option.find_element(By.CSS_SELECTOR, " a").click()
                    break
            assert element_to_be_clickable(self.C_R)

            wait = WebDriverWait(self.driver,10)
            wait.until(expected_conditions.presence_of_element_located(self.Jd_text))

            self.driver.find_element(*self.Jd_text).click()
            self.driver.find_element(*self.resume_upload).send_keys(file_path)
            Job_dis =self.driver.find_element(*self.jd_description)
            Job_dis.send_keys(long_description)
            self.driver.find_element(*self.jd_analyz_button).click()
            wait = WebDriverWait(self.driver, 10)
            wait.until(expected_conditions.presence_of_element_located(self.jd_text_visible))
            JD_Text= self.driver.find_element(*self.jd_text_visible).text
            print(JD_Text)
            time.sleep(5)
            wait = WebDriverWait(self.driver, 10)
            wait.until(expected_conditions.visibility_of_element_located(self.jd_over_all_s))
            timestamp=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.driver.get_screenshot_as_file(f"{folder_path}/JD_SCORE_{timestamp}.png")
            Over_all_score = self.driver.find_element(*self.jd_over_all_s).text
            Skills_score = self.driver.find_element(*self.jd_skills_s).text
            Experience_score = self.driver.find_element(*self.jd_experience_s).text
            Education_score = self.driver.find_element(*self.jd_education_s).text
            print(f"Over_all_score :{Over_all_score}\nSkillScore:{Skills_score}\nExperienceScore:{Experience_score}\nEducationScore{Education_score}")


        except Exception as e:
            print(f"careersync_issue: {e}")
            raise

def test_analysing_JD(intiallizing,student_login):

    JD = JD_parsing(intiallizing)
    JD.test_jd_parsing()


