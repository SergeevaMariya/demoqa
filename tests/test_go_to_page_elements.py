import time

from conftest import browser
from pages.elements_page import ElementsPage
from pages.demoqa import Demoqa


def test_go_to_page_elements(browser):
    el_page = ElementsPage(browser)
    demo_page = Demoqa(browser)
    demo_page.visit()
    assert demo_page.equal_url()
    time.sleep(5)
    demo_page.btn_elements.click()

    assert el_page.equal_url()
