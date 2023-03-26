from pages.accordian import Accordian
import time


def visible_accordian(browser):
    demo_page = Accordian(browser)
    demo_page.visit()
    assert demo_page.text_elements.visible()
    demo_page.btn_elements.click()
    time.sleep(2)
    assert not demo_page.text_elements.visible()


def test_visible_accordian_default(browser):
    demo_page = Accordian(browser)
    demo_page.visit()

    assert not demo_page.text_elements1.visible()
    assert not demo_page.text_elements2.visible()
    assert not demo_page.text_elements3.visible()
