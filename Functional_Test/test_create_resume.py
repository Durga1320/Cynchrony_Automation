import datetime

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("intiallizing","student_login")
class Resume:
    def __init__(self,driver):
        self.driver = driver
        course_name = "Business"


        self.career_sync = (By.XPATH,"//ul[@class='space-y-6']/li[2]/button/div")
        self.create_resume_button = (By.CSS_SELECTOR,"ul[class='mt-2 ml-9 space-y-1'] li")
        self.visibility_text = (By.XPATH, "//div[@class='space-y-4']/h2")
        self.fullname=(By.CSS_SELECTOR,"input[placeholder ='John Doe']")
        self.email =(By.CSS_SELECTOR, "input[id='email']")
        self.phone_number=(By.CSS_SELECTOR, "input[id='phone']")
        self.linked_in =(By.CSS_SELECTOR,"input[id='linkedin']")
        self.git_hub = (By.CSS_SELECTOR,"input[id='github']")
        self.personal_website=(By.CSS_SELECTOR,"input[id='website']")
        self.proffesional_obj  = (By.CSS_SELECTOR, " textarea[id = 'objective']")
        self.save_button =(By.XPATH,"//div[@class='flex justify-end space-x-2 pt-4']/button[2]")

        #Education
        self.Education_button=(By.XPATH, "//div[@class='mb-6']/nav/div[2]/button")
        self.college_name = (By.CSS_SELECTOR, "input[id='school']")
        self.degree =(By.CSS_SELECTOR,"input[id='degree']")
        self.field = (By.XPATH, "//div[@class='space-y-2'][3]/button")
        self.field_of_study =(By.XPATH,f"//span[text()='{course_name}']")
        self.start_date =(By.CSS_SELECTOR,"input[id='startDate']")
        self.End_date=(By.CSS_SELECTOR,"input[id='endDate']")
        self.CGPA=(By.CSS_SELECTOR,"input[id='gpa']")
        self.course_discription=(By.XPATH,"//div[@class='space-y-2']/textarea[@id='description']")

        # Experience
        self.experience_button =(By.XPATH,"//div[@class='flex items-center']/button[text()='Experience']")
        self.company_name =(By.CSS_SELECTOR,"input[id='company']")
        self.postion=(By.CSS_SELECTOR,"input[id='position']")
        self.location=(By.CSS_SELECTOR,"input[id='location']")
        self.exp_start_date =(By.CSS_SELECTOR,"input[id='startDate']")
        self.exp_end_date =(By.CSS_SELECTOR,"input[id='endDate']")
        self.exp_discription=(By.XPATH,"//textarea[@id='description']")
        self.exp_save_button = (By.XPATH,"//div[@class='flex justify-end space-x-2 pt-4']/button[2]")

        #Skills
        self.Skill_button =(By.XPATH,"//div[@class='flex items-center']/button[text()='Skills']")
        self.Tech_skills =(By.CSS_SELECTOR,"input[id='technical']")
        self.Tech_button =(By.XPATH,"(//div[@class='flex gap-2']/button)[1]")
        self.soft_skill =(By.CSS_SELECTOR,"input[id='soft']")
        self.soft_button =(By.XPATH,"(//div[@class='flex gap-2']/button)[2]")
        self.language = (By.CSS_SELECTOR,"input[id='languages']")
        self.langu_button =(By.XPATH,"(//div[@class='flex gap-2']/button)[3]")
        self.Tool =(By.CSS_SELECTOR,"input[id='tools']")
        self.tool_button =(By.XPATH,"(//div[@class='flex gap-2']/button)[4]")
        self.reset =(By.XPATH,"(//div[@class='flex justify-end space-x-2 pt-4']/button)[1]")
        self.entered_skill =(By.XPATH,"(//div[@class='flex flex-wrap gap-2 mt-2']/div)[1]")

        #Certifications
        self.certificate_button =(By.XPATH,"//div[@class='flex items-center']/button[text()='Certifications']")
        self.certify_name =(By.CSS_SELECTOR,"input[id='name']")
        self.certify_issuer =(By.CSS_SELECTOR,"input[id='issuer']")
        self.certify_date =(By.CSS_SELECTOR,"input[id='date']")
        self.certify_discription =(By.CSS_SELECTOR,"textarea[id='description']")

        #Award and Achievements
        self.award_button =(By.XPATH,"//div[@class='flex items-center']/button[text()='Awards & Achievements']")
        self.award_title =(By.CSS_SELECTOR,"input[id='title']")
        self.award_org =(By.CSS_SELECTOR,"input[name='issuer']")
        self.award_issued_date =(By.CSS_SELECTOR,"input[name='date']")
        self.award_discription =(By.CSS_SELECTOR,"textarea[name='description']")

        #Others
        self.others_button = (By.XPATH,"//div[@class='flex items-center']/button[text()='Others']")
        self.intrest_area =(By.CSS_SELECTOR,"input[id='interests']")
        self.intrest_add =(By.XPATH,"//div[@class='flex gap-2']/button[text()='Add']")
        self.add_reference_button =(By.XPATH,"(//div[@class='space-y-4']/div/button)[1]")
        self.add_name =(By.CSS_SELECTOR,"input[name='name']")
        self.postion_ref =(By.CSS_SELECTOR,"input[name='position']")
        self.ref_company_name =(By.CSS_SELECTOR,"input[name='company']")
        self.ref_contact =(By.CSS_SELECTOR,"input[id='contact']")
        self.custom_sec_ref=(By.XPATH,"(//div[@class='space-y-4']/div/button)[3]")
        self.custome_title =(By.CSS_SELECTOR,"input[id='title']")
        self.custome_content =(By.CSS_SELECTOR,"textarea[id='content']")

        #Download Resume PDF ,DOC, Textfile
        self.Download_resume_pdf =(By.XPATH,"//div[@class='flex space-x-2']/button[1]")
        self.Download_resume_Doc =(By.XPATH,"//div[@class='flex space-x-2']/button[2]")
        self.Download_resume_textfile =(By.XPATH,"//button[text()='Text File']")







    def test_Create_Resume(self):
        try:

           self.driver.find_element(*self.career_sync).click()
           list_of_options = self.driver.find_elements(*self.create_resume_button)
           for option in list_of_options:
               if option.text == "Create Resume":
                   self.C_R=option.find_element(By.CSS_SELECTOR," a").click()
                   break
           assert element_to_be_clickable(self.C_R)
           wait = WebDriverWait(self.driver,15)
           wait.until(expected_conditions.visibility_of_element_located(self.visibility_text))
        except Exception as e:
            print(f"careersync_issue: {e}")
            raise


    def test_your_details(self):
        try:

            self.driver.find_element(*self.fullname).send_keys("Durga prasad")
            self.driver.find_element(*self.email).send_keys("durgaprasadkatakamsetti13@gmail.com")
            self.driver.find_element(*self.phone_number).send_keys("9381929292")
            self.driver.find_element(*self.linked_in).send_keys("linked_in")
            self.driver.find_element(*self.git_hub).send_keys("github.com/durga1")
            self.driver.find_element(*self.personal_website).send_keys("cynchrony.in")
            self.driver.find_element(*self.proffesional_obj).send_keys("I am a Automation tester . Having over 3+ years of exp")
            self.driver.find_element(*self.save_button).click()

            #wait=WebDriverWait(self.driver,10)
            #wait.until(expected_conditions.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            self.driver.execute_script("window.scrollTo(300,0)")
        except Exception as e:
            print(f"issue in personal_details_section: {e}")
            raise

    def test_Education_info(self):

        try:

            about_course ="""Business is the activity of producing, buying, or selling goods and services to earn a profit.
            It involves understanding customer needs and delivering value through products or solutions.
            Successful businesses balance innovation, operations, and strategy to grow sustainably"""


            self.driver.find_element(*self.Education_button).click()
            self.driver.find_element(*self.college_name).send_keys("Sagi Ramakrishnam Raju College")
            self.driver.find_element(*self.degree).send_keys("B.Tech")
            self.driver.find_element(*self.field).click()
            wait = WebDriverWait(self.driver,5)
            wait.until(expected_conditions.presence_of_element_located(self.field_of_study))
            self.driver.find_element(*self.field_of_study).click()
            Start_Date=self.driver.find_element(*self.start_date)
            Start_Date.send_keys("10062017")
            Start_Date.click()
            #timestamp=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            #self.driver.get_screenshot_as_file(f"{folder_path}/startdate_{timestamp}.png")
            End_Date=self.driver.find_element(*self.End_date)
            End_Date.send_keys("31072021")
            End_Date.click()
            self.driver.find_element(*self.CGPA).send_keys("7.2")
            Course=self.driver.find_element(*self.course_discription)
            Course.send_keys(about_course)
            self.driver.find_element(*self.save_button).click()
            alert = self.driver.switch_to.alert
            alert.accept()
            self.driver.execute_script("window.scrollTo(300,0)")

        except Exception as e:
            print(f"issue in education_section: {e}")
            raise

    def test_Experience_info(self):

        try:
            role_discription="""
            An Automation Engineer designs, develops, and maintains automated systems to improve efficiency and reduce manual effort.
            They work with tools, scripts, and frameworks to automate testing, deployment, or industrial processes.
            Their role bridges software engineering and operations to ensure quality, speed, and reliability.
            """
            self.driver.find_element(*self.experience_button).click()
            self.driver.find_element(*self.company_name).send_keys("Capgemini")
            self.driver.find_element(*self.postion).send_keys("Sr Analyst")
            self.driver.find_element(*self.location).send_keys("Hyderabad")
            exp_start_date= self.driver.find_element(*self.exp_start_date)
            exp_start_date.send_keys("03022022")
            exp_start_date.click()
            exp_end_date = self.driver.find_element(*self.exp_end_date)
            exp_end_date.send_keys("05022025")
            Exp_Discr =self.driver.find_element(*self.exp_discription)
            Exp_Discr.send_keys(role_discription)
            self.driver.find_element(*self.exp_save_button).click()
            alert = self.driver.switch_to.alert
            alert.accept()
            self.driver.execute_script("window.scrollTo(300,0)")
        except Exception as e:
           print(f"issue in Experience_section: {e}")
           raise

    def test_skill_info(self):
        try:

            self.driver.find_element(*self.Skill_button).click()
            self.driver.find_element(*self.Tech_skills).send_keys("Python")
            self.driver.find_element(*self.Tech_button).click()
            self.driver.find_element(*self.soft_skill).send_keys("English")
            self.driver.find_element(*self.soft_button).click()
            self.driver.find_element(*self.language).send_keys("Telugu")
            self.driver.find_element(*self.langu_button).click()
            self.driver.find_element(*self.Tool).send_keys("Tosca")
            self.driver.find_element(*self.tool_button).click()
            self.driver.find_element(*self.save_button).click()
            alert = self.driver.switch_to.alert
            alert.accept()
            self.driver.find_element(*self.reset).click()
            alert.accept()
            #time.sleep(5)
            self.driver.execute_script("window.scrollTo(300,0)")

            #entered_Skill= self.driver.find_element(*self.entered_skill)

            #assert not entered_Skill.is_displayed(),"Element should not be visible"

        except Exception as e:
            print(f"Login failed: {e}")
            raise

    def test_Certification(self):

        try:
            self.driver.find_element(*self.certificate_button).click()
            self.driver.find_element(*self.certify_name).send_keys("Anirudh")
            self.driver.find_element(*self.certify_issuer).send_keys("Udemy")
            self.driver.find_element(*self.certify_date).send_keys("10092021")
            self.driver.find_element(*self.certify_discription).send_keys("python certification")
            self.driver.find_element(*self.save_button).click()
            alert = self.driver.switch_to.alert
            alert.accept()
            time.sleep(5)

        except Exception as e:
            print(f"issue in Cerification_section : {e}")

    def test_Awards_Achievements(self):

        try:
            self.driver.find_element(*self.award_button).click()
            self.driver.find_element(*self.award_title).send_keys("Star_award")
            self.driver.find_element(*self.award_org).send_keys("accenture")
            self.driver.find_element(*self.award_issued_date).send_keys("11092024")
            self.driver.find_element(*self.award_discription).send_keys("Quaterly Award")
            self.driver.find_element(*self.save_button).click()
            alert = self.driver.switch_to.alert
            alert.accept()
        except Exception as e:
            print(f"issue Awards&Achievements_section : {e}")

    def test_Others(self):
        try:
            self.driver.find_element(*self.others_button).click()
            self.driver.find_element(*self.intrest_area).send_keys("Automation_testing")
            self.driver.find_element(*self.intrest_add).click()
            self.driver.find_element(*self.add_reference_button).click()
            self.driver.find_element(*self.add_name).send_keys("Devops")
            self.driver.find_element(*self.postion_ref).send_keys("Azure_Devops Engineer")
            self.driver.find_element(*self.ref_company_name).send_keys("Accenture")
            self.driver.find_element(*self.ref_contact).send_keys("9842412345")
            self.driver.find_element(*self.custom_sec_ref).click()
            self.driver.find_element(*self.custome_title).send_keys("Angular developer")
            self.driver.find_element(*self.custome_content).send_keys("develop the application")
            self.driver.find_element(*self.save_button).click()
            alert = self.driver.switch_to.alert
            alert.accept()
        except Exception as e:
            print(f"issue in Awards&Achievements_section : {e}")

    def download_resume_pdf(self):
        try:
            self.driver.find_element(*self.Download_resume_pdf).click()
            alert = self.driver.switch_to.alert
            alert.accept()
            time.sleep(8)

        except Exception as e:
            print(f"issue when downloading resume: {e}")

    @pytest.mark.skip
    def download_resume_DOC(self):
        try:
            self.driver.find_element(*self.Download_resume_Doc).click()

        except Exception as e:
            print(f"issue when downloading resume: {e}")

    @pytest.mark.skip
    def download_resume_textfile(self):
        try:
            self.driver.find_element(*self.Download_resume_textfile).click()

        except Exception as e:
            print(f"issue when downloading resume: {e}")








def test_creating_resume(intiallizing,student_login):

    Resume_instance = Resume(intiallizing)
    Resume_instance.test_Create_Resume()
    Resume_instance.test_your_details()
    Resume_instance.test_Education_info()
    Resume_instance.test_Experience_info()
    Resume_instance.test_skill_info()
    Resume_instance.test_Certification()
    Resume_instance.test_Awards_Achievements()
    Resume_instance.test_Others()
    Resume_instance.download_resume_pdf()
    Resume_instance.download_resume_DOC()



