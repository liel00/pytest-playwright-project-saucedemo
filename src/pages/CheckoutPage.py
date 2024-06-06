from playwright.sync_api import expect


class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self._first_name_write = page.locator("//input[@id='first-name']")
        self._last_name_write = page.locator("//input[@id='last-name']")
        self._zip_code_write = page.locator("//input[@id='postal-code']")
        self._continue_button = page.locator("//input[@id='continue']")
        self._finish_button = page.locator("//button[@id='finish']")
        self._massage_thank = page.locator("//h2[contains(text(),'Thank you for your order!')]")

    def first_name_write(self, first_name):
        self._first_name_write.fill(first_name)

    def last_name_write(self, last_name):
        self._last_name_write.fill(last_name)

    def zip_code_write(self, zip_code):
        self._zip_code_write.fill(zip_code)

    def click_continue(self):
        self._continue_button.click()

    def click_finish_button(self):
        self._finish_button.click()

    def check_massage_thank_for_your_order(self, massage):
        expect(self._massage_thank).to_contain_text(massage)
