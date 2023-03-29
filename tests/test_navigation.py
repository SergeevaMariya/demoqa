from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage


def test_navigation(browser):
    demo_page = Demoqa(browser)


    demo_page.visit()
    demo_page.btn_elements.scroll_two_element()
    demo_page.btn_elements.click()
    browser.refresh()
    browser.back()
    browser.forward()
    demo_pages = ElementsPage(browser)
    assert  demo_pages.equal_url()
