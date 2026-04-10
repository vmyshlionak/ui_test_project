from pages.base_page import BasePage
from pages.triangle_page import TrianglePage


def test_triangle_page(driver):
    triangle_page = TrianglePage(driver)
    triangle_page.open_page()
    triangle_page.check_h1_title()
