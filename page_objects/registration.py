from page_objects.base_page import BasePage
from locators.login_locators import locators
from locators.registration_locators import registration_locators
import test_data.login_data
import test_data.registration_data


class Registration(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    # move below 3 codes to login
    def click_CreateAnAccountBtn(self):
        self.do_click(locators.createAccount_button_ID)

    def enter_invalidEmail(self):
        self.do_sendKeys(locators.emailCreate_ID, test_data.login_data.invalidEmail)

    def enter_validEmail(self, email):
        self.do_sendKeys(locators.emailCreate_ID, email)

    #     Registration starts from here

    def enter_firstName(self):
        self.do_clear(registration_locators.firstname)
        self.do_sendKeys(registration_locators.firstname, test_data.registration_data.firstname)

    def enter_lastname(self):
        self.do_clear(registration_locators.lastname)
        self.do_sendKeys(registration_locators.lastname, test_data.registration_data.lastname)

    def enter_email(self, email):
        self.do_sendKeys(registration_locators.email, email)

    def enter_pwd(self):
        self.do_sendKeys(registration_locators.pwd, test_data.registration_data.pwd)

    def enter_address_firstname(self):
        self.do_sendKeys(registration_locators.address_firstname, test_data.registration_data.address_firstname)

    def enter_address_lastname(self):
        self.do_sendKeys(registration_locators.address_lastname, test_data.registration_data.address_lastname)

    def enter_address(self):
        self.do_sendKeys(registration_locators.address1, test_data.registration_data.address1)

    def enter_city(self):
        self.do_sendKeys(registration_locators.city, test_data.registration_data.city)

    def select_state(self):
        self.do_click(registration_locators.state)
        self.do_click(registration_locators.stateValue)

    def enter_postcode(self):
        self.do_sendKeys(registration_locators.postcode, test_data.registration_data.postcode)

    def enter_phone_mobile(self):
        self.do_sendKeys(registration_locators.phone_mobile, test_data.registration_data.phone_mobile)

    def click_register(self):
        self.do_click(registration_locators.register)
