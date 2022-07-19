import time
from page_objects.base_page import BasePage
from locators.products_locators import products_locators, products_delete_locators
from selenium.common.exceptions import NoSuchFrameException


class Products(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def click_AddToCart(self, dress):
        self.do_click(dress)

    def click_product(self, by_locator):
        self.do_click(by_locator)

    def switchToIframe(self):
        try:
            self.driver.switch_to.frame(1)
        except NoSuchFrameException:
            print("No element found from except")

    def switchToDefaultFrame(self):
        self.driver.switch_to.default_content()

    def click_addToCart(self):
        self.switchToIframe()
        time.sleep(3)
        self.do_click(products_locators.addToCart)
        self.switchToDefaultFrame()

    def click_continueShopping(self):
        self.do_click(products_locators.continueShopping)

    def click_cart(self):
        self.do_click(products_delete_locators.cart)

    def click_blouseDelete(self):
        self.do_click(products_delete_locators.blouseDelete)

