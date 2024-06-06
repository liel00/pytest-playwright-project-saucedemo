from src.pages.CartPage import CartPage
from src.pages.CheckoutPage import CheckoutPage
from src.pages.LoginPage import LogInPage
from src.pages.ProductListPage import ProductListPage


# The test checks an order on the website
def test_place_order(set_up_tear_down, page) -> None:
    login_page = LogInPage(page)
    product_page = ProductListPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    login_page.write_to_a_username("standard_user")
    login_page.write_to_a_password("secret_sauce")
    login_page.click_button_login()
    product_page.add_sauce_labs_backpack_on_cart()
    product_page.click_shopping_cart()
    cart_page.check_product_in_card("Sauce Labs Backpack")
    cart_page.check_price_in_card("$29.99")
    cart_page.click_checkout_button()
    checkout_page.first_name_write("Test123")
    checkout_page.last_name_write("Test456")
    checkout_page.zip_code_write("1246")
    checkout_page.click_continue()
    checkout_page.click_finish_button()
    checkout_page.check_massage_thank_for_your_order("Thank you for your order!")
