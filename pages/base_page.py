from selenium.common import NoSuchElementException


class BasePage():

    base_url = 'https://testpages.eviltester.com/apps'
    page_url = None

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('No such url')

    def find(self, locator: tuple):
      return self.driver.find_element(*locator)
