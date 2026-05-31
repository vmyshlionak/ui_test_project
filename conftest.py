import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.customer_login import CustomerLogin
from pages.triangle_page import TrianglePage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver

@pytest.fixture
def login_page(driver):
    return CustomerLogin(driver)

@pytest.fixture
def triangle_page(driver):
    return TrianglePage(driver)