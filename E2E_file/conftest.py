import pytest
from selenium import webdriver
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",action="store",default=False,help="browser selection"
    )

@pytest.fixture(scope='function')

def browser_instance(request):
    browser_name = request.config.getoption("--browser_name") # it will get the inpiut at run time

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "Edge":
        driver = webdriver.Edge()
    yield driver
    driver.quit()
