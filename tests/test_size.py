import time

from pages.demoqa import Demoqa


def test_window_size(browser):
    demo_page = Demoqa(browser)
    demo_page.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)
