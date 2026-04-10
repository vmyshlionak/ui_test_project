import pytest
from selenium import webdriver

from pages.customer_login import CustomerLogin
from pages.triangle_page import TrianglePage


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    return chrome_driver

@pytest.fixture
def login_page(driver):
    return CustomerLogin(driver)

@pytest.fixture
def triangle_page(driver):
    return TrianglePage(driver)