from page_objects.base_page import BasePage
from locators.login_locators import locators
import test_data.login_data
import test_data.registration_data
from locators.products_locators import products_locators


class Login(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    # move below 3 codes to login
    def click_signIn(self):
        self.do_click(locators.SignInButton)

    def enter_invalidEmail(self):
        self.do_sendKeys(locators.email, test_data.login_data.invalidEmail)

    def enter_invalidpwd(self):
        self.do_sendKeys(locators.pwd, test_data.login_data.invalidpwd)

    def enter_validEmail(self):
        self.do_sendKeys(locators.email, test_data.login_data.validemail)

    def enter_validpwd(self):
        self.do_sendKeys(locators.pwd, test_data.login_data.validpwd)

    def click_home(self):
        self.do_click(products_locators.home)

    def login(self):
        self.enter_validEmail()
        self.enter_validpwd()
        self.click_signIn()
        self.click_home()
