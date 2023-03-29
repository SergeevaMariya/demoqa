from pages.modal_dialogs import ModalDialogs
from pages.demoqa import Demoqa


def test_modal_elements(browser):
    demoqa_modal = ModalDialogs(browser)
    demoqa_modal.visit()
    assert demoqa_modal.btn_submenu.check_count_elements(5)


def test_navigation_modal(browser):
    demoqa_modal = ModalDialogs(browser)
    demoqa_page = Demoqa(browser)
    demoqa_modal.visit()
    browser.refresh()
    demoqa_modal.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert demoqa_page.equal_url()
    assert browser.title == demoqa_page.pageData['title']
    browser.set_window_size(1000, 1000)