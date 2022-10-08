from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print("Launching Chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        print("Launching Firefox browser")
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver


def pytest_addoption(parser):  # This will get the value from command line
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to the setup method
    return request.config.getoption("--browser")

### For generating Pytest HTML reports ###

#customize the report name
# def pytest_html_report_title(report):
#     report.title = "My very own title!"

def pytest_configure(config):
    config._metadata["Project Name"] = "Cura Healthcare services"
    config._metadata["Module Name"] = "Book appointment"


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)























