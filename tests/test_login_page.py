from pages.customer_login import CustomerLogin


def test_incorrect_login(driver):
    login_page = CustomerLogin(driver)
    login_page.open_page()
    login_page.scroll_below()
    login_page.login_and_password('test', 'test')
    login_page.check_error_message('Login Details Incorrect')

