from src.pages.LoginPage import LogInPage
from src.pages.ProductListPage import ProductListPage

#Test checks logout from the user
def test_logout(set_up_tear_down, page) -> None:
    login_page = LogInPage(page)
    product_page = ProductListPage(page)
    login_page.write_to_a_username("standard_user")
    login_page.write_to_a_password("secret_sauce")
    login_page.click_button_login()
    product_page.click_nev_bar()
    product_page.click_logout()
    login_page.swag_labs_logo_visible()
