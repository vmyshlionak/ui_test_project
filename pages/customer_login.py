from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import login_page_locs as loc
from time import sleep

class CustomerLogin(BasePage):
    page_url = '/simulated-login/'

    def scroll_below(self):
        self.driver.execute_script('window.scrollTo(500, document.body.scrollHeight);')
        sleep(2)

    def scroll_to_element_js(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def login_and_password(self, username, password):
        username_field = self.find(loc.username_loc)
        self.scroll_to_element_js(username_field)
        username_field.send_keys(username)
        password_field = self.find(loc.password_loc)
        password_field.send_keys(password)
        # login_button = self.find(loc.login_button_loc)
        # self.scroll_to_element_js(login_button)
        # login_button.click()
        self.find(loc.login_button_loc).click()

    def check_error_message(self, error_message):
        message = self.find(loc.message_loc).text
        assert message == 'Login Details Incorrect'

