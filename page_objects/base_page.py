from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import waits


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_clear(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def do_click(self, by_locator):
        waits.wait_until_element_is_clickable(self.driver, by_locator).click()

    def do_sendKeys(self, by_locator, text):
        waits.wait_until_element_is_clickable(self.driver, by_locator).send_keys(text)

    def elementExist(self, by_locator):
        try:
            element = waits.wait_until_visibility_of_element_located(self.driver, by_locator)
            return element
        except (TimeoutException, NoSuchElementException):
            return False

    def hoverElement(self, by_locator):
        self.driver.execute_script("window.scrollBy(0,700);")
        try:
            element = ActionChains(self.driver)
            moveTo = self.driver.find_element(by_locator)
            element.move_to_element(moveTo).perform()
            print("hovering done")
        except NoSuchElementException:
            print("No element found on hovering")

    def scrolling(self, value):
        self.driver.execute_script("window.scrollBy(0,value);")
