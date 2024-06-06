class ProductListPage:
    def __init__(self, page):
        self.page = page
        self._logo_product = page.locator("//span[contains(text(),'Products')]")
        self._nev_bar = page.locator("//button[@id='react-burger-menu-btn']")
        self._logout = page.locator("//a[@id='logout_sidebar_link']")
        self._shopping_cart = page.locator("[data-test=\"shopping-cart-link\"]")
        self._add_sauce_labs_backpack = page.locator("//button[@id='add-to-cart-sauce-labs-backpack']")

    def check_logo_product(self):
        return self._logo_product.is_visible()

    def click_nev_bar(self):
        self._nev_bar.click()

    def click_logout(self):
        self._logout.click()

    def add_sauce_labs_backpack_on_cart(self):
        self._add_sauce_labs_backpack.click()

    def click_shopping_cart(self):
        self._shopping_cart.click()
