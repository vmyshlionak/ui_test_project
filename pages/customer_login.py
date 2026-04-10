from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import login_page_locs as loc

class CustomerLogin(BasePage):
    page_url = '/simulated-login/'

    def scroll_below(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def login_and_password(self, username, password):
        username_field = self.find(loc.username_loc)
        username_field.send_keys(username)
        password_field = self.find(loc.password_loc)
        password_field.send_keys(password)
        self.find(loc.login_button_loc).click()

    def check_error_message(self, error_message):
        message = self.find(loc.message_loc).text
        assert message == 'Login Details Incorrect'

