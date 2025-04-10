import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("intiallizing","student_login")
class Resume:
    def __init__(self,driver):
        self.driver = driver
        self.career_sync = (By.XPATH,"//ul[@class='space-y-6']/li[2]/button/div")
        self.create_resume_button = (By.CSS_SELECTOR,"ul[class='mt-2 ml-9 space-y-1'] li")
        self.visibility_text = (By.XPATH, "//div[@class='space-y-4']/h2")



    def test_Create_Resume(self):

        self.driver.find_element(*self.career_sync).click()
        list_of_options = self.driver.find_elements(*self.create_resume_button)
        #print(len(list_of_options))
        for option in list_of_options:
            #print(option.text)
            if option.text == "Create Resume":
                self.C_R=option.find_element(By.CSS_SELECTOR," a").click()
                break
        assert element_to_be_clickable(self.C_R)
        wait = WebDriverWait(self.driver,15)
        wait.until(expected_conditions.visibility_of_element_located(self.visibility_text))



def test_creating_resume(intiallizing,student_login):

    Resume_instance = Resume(intiallizing)
    Resume_instance.test_Create_Resume()



