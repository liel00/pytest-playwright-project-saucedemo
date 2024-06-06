from playwright.sync_api import expect


class CartPage:
    def __init__(self, page):
        self.page = page
        self._price_in_cart = page.locator("[data-test=\"inventory-item-price\"]")
        self._name_sauce_labs_backpack = page.locator("[data-test=\"item-4-title-link\"]")
        self._checkout_button = page.locator("//button[@id='checkout']")

    def check_price_in_card(self, price):
        expect(self._price_in_cart).to_contain_text(price)

    def check_product_in_card(self, product):
        expect(self._name_sauce_labs_backpack).to_contain_text(product)

    def click_checkout_button(self):
        self._checkout_button.click()
