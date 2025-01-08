import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


@pytest.fixture(scope="session")
def setup(browser):
    # Browser initialization with options to disable notifications
    if browser == 'chrome':
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 2
        })
        driver = webdriver.Chrome(options=chrome_options)
        print("Launching Chrome browser with notifications disabled")

    elif browser == 'firefox':
        firefox_options = FirefoxOptions()
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("dom.webnotifications.enabled", False)
        firefox_profile.set_preference("dom.webnotifications.serviceworker.enabled", False)
        driver = webdriver.Firefox(options=firefox_options)
        print("Launching Firefox browser with notifications disabled")

    elif browser == 'edge':
        edge_options = EdgeOptions()
        edge_options.add_argument("--disable-notifications")
        driver = webdriver.Edge(options=edge_options)
        print("Launching Edge browser with notifications disabled")

    else:
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 2
        })
        driver = webdriver.Chrome(options=chrome_options)
        print("Launching default browser Chrome with notifications disabled")

    driver.maximize_window()
    driver.implicitly_wait(5)

    # Return driver to test cases
    yield driver

    # Teardown after all tests are done
    print("Closing the browser")
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome, firefox, edge")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
