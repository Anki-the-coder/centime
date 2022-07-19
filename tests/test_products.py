import pytest
from page_objects.products import Products
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


@pytest.fixture
def products_Fix(driver):
    return Products(driver)


class Test_products(BaseTest):

    @pytest.mark.positive
    def test_addDeleteItemToCart(self, base_fix, login_Fix, products_Fix):
        login_Fix.login()
        products_Fix.click_product(products_locators.blouse)
        products_Fix.click_addToCart()
        assert base_fix.elementExist(products_locators.OKIcon)
        base_fix.do_click(products_locators.continueShopping)
        products_Fix.click_product(products_locators.printedDress)
        products_Fix.click_addToCart()
        assert base_fix.elementExist(products_locators.OKIcon)
        base_fix.do_click(products_locators.continueShopping)
        products_Fix.click_cart()
        products_Fix.click_blouseDelete()
        assert not base_fix.elementExist(products_locators.OKIcon)