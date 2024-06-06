import logging


import pytest

from src.pages.LoginPage import LogInPage
from src.pages.ProductListPage import ProductListPage
from src.utils.data import testing_data


# Test for checking illegal entries (6 Tests)
# Checks the login attempt error messages
@pytest.mark.parametrize("username, password, error_message", testing_data)
def test_not_valid_login_scenarios(set_up_tear_down, page, username: str, password: str, error_message: str) -> None:
    login_page = LogInPage(page)
    login_page.write_to_a_username(username)
    login_page.write_to_a_password(password)
    login_page.click_button_login()
    assert login_page.massage_error_visible()
    login_page.check_massage_error(error_message)


# Connect with a real user and test it by checking the logo of the products
def test_valid_login_scenarios_standard_user(set_up_tear_down, page) -> None:
    login_page = LogInPage(page)
    product_page = ProductListPage(page)
    login_page.write_to_a_username("standard_user")
    login_page.write_to_a_password("secret_sauce")
    login_page.click_button_login()
    assert product_page.check_logo_product()
