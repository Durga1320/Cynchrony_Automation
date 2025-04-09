import time
import os
import sys
import pytest
from selenium import webdriver
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Cycnchrony_POM.Dashboard_page import Dashboard_Page
from Cycnchrony_POM.Login_page import Login_Page


def test_Cynchrony_E2E(browser_instance):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    #driver = browser_instance
    driver.get("https://cynchrony.in/")
    driver.maximize_window()
    driver.implicitly_wait(5)
   # time.sleep(5)

    loginpage = Login_Page(driver)
    Dashboardpage=loginpage.student_login()
    Dashboardpage.student_Dashboard()
    Dashboardpage.ATS_Analysis()






