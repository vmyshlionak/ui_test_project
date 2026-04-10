from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import triangle_page_locs as locs

class TrianglePage(BasePage):

    header_title = 'Triangle'
    page_url = '/triangle/'

    def check_h1_title(self):
        header = self.find(locs.header_loc)
        assert header.text == self.header_title

