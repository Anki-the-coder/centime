import pytest
from locators.login_locators import locators
from tests.test_base import BaseTest
from page_objects.base_page import BasePage
from page_objects.login import Login
from locators.products_locators import products_locators


@pytest.fixture
def base_fix(driver):
    return BasePage(driver)


@pytest.fixture
def login_Fix(driver):
    return Login(driver)


class Test_log(BaseTest):

    @pytest.mark.negative
    def test_emptyLogin(self, base_fix, login_Fix):
        login_Fix.click_signIn()
        assert base_fix.elementExist(locators.emailAddressRequired)

    @pytest.mark.negative
    def test_invalidLogin(self, base_fix, login_Fix):
        login_Fix.enter_invalidEmail()
        login_Fix.enter_invalidpwd()
        login_Fix.click_signIn()
        assert base_fix.elementExist(locators.invalidEmailMessage)

    @pytest.mark.positive
    def test_validLogin(self, base_fix, login_Fix):
        login_Fix.enter_validEmail()
        login_Fix.enter_validpwd()
        login_Fix.click_signIn()
        assert base_fix.elementExist(products_locators.signOut)
