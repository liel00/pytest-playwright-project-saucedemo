from playwright.sync_api import expect


class LogInPage:
    def __init__(self, page):
        self.page = page
        self._username = page.locator("//input[@id='user-name']")
        self._password = page.locator("//input[@id='password']")
        self._login_button = page.locator("[data-test=\"login-button\"]")
        self._error_message = page.locator("[data-test=\"error\"]")
        self._swag_labs_logo = page.locator("//div[contains(text(),'Swag Labs')]")

    def write_to_a_username(self, text):
        self._username.fill(text)

    def write_to_a_password(self, text):
        self._password.fill(text)

    def click_button_login(self):
        self._login_button.click()

    def massage_error_visible(self):
        return self._error_message.is_visible()

    def check_massage_error(self, check_message):
        expect(self._error_message).to_contain_text(check_message)

    def swag_labs_logo_visible(self):
        self._swag_labs_logo.is_visible()
