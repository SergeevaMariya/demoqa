from pages.elements_page import ElementsPage
import time


def test_visible_btn_sidebar(browser):
    demo_elements = ElementsPage(browser)
    demo_elements.visit()
    # demo_elements.btn_sidebar_first.click()
    time.sleep(3)
    # assert demo_elements.btn_sidebar_first_textbox.exist()
    assert demo_elements.btn_sidebar_first_textbox.visible()

def test_not_visible_btn_sidebar(browser):
    demo_elements = ElementsPage(browser)
    demo_elements.visit()
    assert demo_elements.btn_sidebar_first_checkbox.visible()
    demo_elements.btn_sidebar_first.click()
    time.sleep(2)
    assert not demo_elements.btn_sidebar_first_checkbox.visible()

