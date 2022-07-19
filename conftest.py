import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from utils import waits
from test_data import login_data
from locators.login_locators import locators


@pytest.fixture()
def init_driver(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(login_data.baseURL)
    time.sleep(1)
    waits.wait_until_element_is_clickable(driver, locators.signIn).click()
    request.cls.driver = driver

    yield
    driver.close()


@pytest.fixture()
def driver(request):
    return request.cls.driver
