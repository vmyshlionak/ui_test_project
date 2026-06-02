import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure
from pages.customer_login import CustomerLogin
from pages.triangle_page import TrianglePage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--start-maximized')
    options.add_argument('--no-sandbox')  # КРИТИЧНО для Docker/Linux
    options.add_argument('--disable-dev-shm-usage')  # КРИТИЧНО для Docker
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-blink-features=AutomationControlled')
    # options.add_argument('--remote-debugging-port=9222') #ломает pytest -v в пайчарме
    # Важно: добавить аргументы для устранения ошибок сессии
    options.add_argument('--disable-crash-reporter')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-in-process-stack-traces')
    options.add_argument('--disable-logging')
    options.add_argument('--log-level=3')  # только критические ошибки
    options.add_argument('--silent')
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    allure.attach(chrome_driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)


@pytest.fixture
def login_page(driver):
    return CustomerLogin(driver)

@pytest.fixture
def triangle_page(driver):
    return TrianglePage(driver)