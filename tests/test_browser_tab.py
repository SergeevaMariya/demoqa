import time
from pages.browser_tab import BrowserTab


def test_browser_tab(browser):
    browser_tab_page = BrowserTab(browser)
    browser_tab_page.visit()
    assert len(browser.window_handles) == 1
    browser_tab_page.new_tab.click()
    # assert browser.current_url == ''
    time.sleep(2)
    assert len(browser.window_handles) == 2
    browser.switch_to.window(browser.window_handles[0])
    assert browser_tab_page.get_url()
    time.sleep(2)

