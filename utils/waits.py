from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_until_element_is_clickable(selenium, by_locator, time_to_wait=10):
    return WebDriverWait(selenium, time_to_wait).until(
        EC.element_to_be_clickable(by_locator))


def wait_until_visibility_of_all_elements_located(selenium, by_locator, time_to_wait=10):
    return WebDriverWait(selenium, time_to_wait).until(
        EC.visibility_of_all_elements_located(by_locator))


def wait_until_visibility_of_element_located(selenium, by_locator, time_to_wait=10):
    return WebDriverWait(selenium, time_to_wait).until(
        EC.visibility_of_element_located(by_locator))


def abc(selenium, by_locator, time_to_wait=10):
    return WebDriverWait(selenium, time_to_wait).until(
        EC.frame_to_be_available_and_switch_to_it(by_locator)
    )





