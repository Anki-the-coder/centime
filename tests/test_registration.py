import pytest
from locators.login_locators import locators
from locators.products_locators import products_locators
from tests.test_base import BaseTest
from utils import random_data
from page_objects.base_page import BasePage
from page_objects.registration import Registration


@pytest.fixture
def registration_Fix(driver):
    return Registration(driver)


@pytest.fixture
def base_fix(driver):
    return BasePage(driver)


class Test_registration(BaseTest):

    @pytest.mark.negative
    def test_emptyRegistration(self, registration_Fix, base_fix):
        registration_Fix.click_CreateAnAccountBtn()
        assert base_fix.elementExist(locators.invalidEmailMessage)

    @pytest.mark.negative
    def test_invalidRegistration(self, registration_Fix, base_fix):
        registration_Fix.enter_invalidEmail()
        registration_Fix.click_CreateAnAccountBtn()
        assert base_fix.elementExist(locators.invalidEmailMessage)

    @pytest.mark.positive
    def test_Registration(self, registration_Fix, base_fix):
        email = random_data.random_alphaNumeric() + '@gmail.com'
        registration_Fix.enter_validEmail(email)
        registration_Fix.click_CreateAnAccountBtn()
        registration_Fix.enter_firstName()
        registration_Fix.enter_lastname()
        registration_Fix.enter_pwd()
        registration_Fix.enter_address()
        registration_Fix.enter_city()
        registration_Fix.select_state()
        registration_Fix.enter_postcode()
        registration_Fix.enter_phone_mobile()
        registration_Fix.click_register()
        assert base_fix.elementExist(products_locators.signOut)


