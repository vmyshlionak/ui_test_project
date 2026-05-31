from pages.locators.login_page_locs import login_button_loc, username_loc

def test_incorrect_login(login_page):
    login_page.open_page()
    login_page.scroll_below()
    login_page.login_and_password('test', 'test')
    login_page.check_error_message('Login Details Incorrect')

