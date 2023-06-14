import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        ser_obj = Service("C:/Users/ADMIN/Downloads/chromedriver.exe")
        driver = webdriver.Chrome(service=ser_obj)
    elif browser_name == 'firefox':
        ser_obj = Service("C:/Users/ADMIN/Downloads/geckodriver.exe")
        driver = webdriver.Firefox(service=ser_obj)
    elif browser_name == 'edge':
        ser_obj = Service("C:/Users/ADMIN/Downloads/msedgedriver.exe")
        driver = webdriver.Edge(service=ser_obj)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
