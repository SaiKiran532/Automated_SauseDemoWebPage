import webbrowser

from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    else:
        driver = webdriver.Edge()
        print("Launching Edge browser")
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")




