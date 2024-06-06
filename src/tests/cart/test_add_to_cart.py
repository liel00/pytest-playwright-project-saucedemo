from src.pages.CartPage import CartPage
from src.pages.LoginPage import LogInPage
from src.pages.ProductListPage import ProductListPage


# The purpose of the test is to verify that a user can successfully log into the website, add a product
# to the shopping cart, and that the product details (name and price) are correctly displayed in the shopping cart.
def test_add_product_in_cart(set_up_tear_down, page) -> None:
    login_page = LogInPage(page)
    product_page = ProductListPage(page)
    cart_page = CartPage(page)
    login_page.write_to_a_username("standard_user")
    login_page.write_to_a_password("secret_sauce")
    login_page.click_button_login()
    product_page.add_sauce_labs_backpack_on_cart()
    product_page.click_shopping_cart()
    cart_page.check_product_in_card("Sauce Labs Backpack")
    cart_page.check_price_in_card("$29.99")
