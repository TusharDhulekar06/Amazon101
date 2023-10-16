import os.path

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from datetime import datetime

@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        service=EdgeService(executable_path=EdgeChromiumDriverManager().install())
        driver=webdriver.Edge(service=service)
        # driver=EdgeService(executable_path=EdgeChromiumDriverManager().install())
        print("Launching Edge browser....... ")
    elif browser == 'firefox':
        service=FirefoxService(executable_path=GeckoDriverManager().install())
        driver=webdriver.Firefox(service=service)
        # driver=FirefoxService(executable_path=GeckoDriverManager().install())
        print("Launching firefox browser....")
    else:
        service=ChromeService(executable_path=ChromeDriverManager().install())
        driver=webdriver.Chrome(service=service)
        # driver=ChromeService(executable_path=ChromeDriverManager().install())
        print("Launching Chrome browser")
    # service=ChromeService(executable_path=ChromeDriverManager().install())
    # driver=webdriver.Chrome(service=service)
    return driver
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
##############Pytest HTML Report###########

# hook to add environment info to Html report
def pytest_configure(config):
    config.metadata['Project Name'] = 'Amazon'
    config.metadata['Module Name'] = 'DataDrivenTest'
    config.metadata['Tester'] = 'Tushar'

# it is hook for delete/Modify Environment info to HTMl report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)

#specify report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%y %H-%M-%S")+".html"

