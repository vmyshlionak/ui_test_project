import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    return chrome_driver