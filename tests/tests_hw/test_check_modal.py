from pages.modal_dialogs import ModalDialogs
import allure
import time
import requests

def test_check_modal(browser):
    check_modal = ModalDialogs(browser)
    check_modal.visit()

    assert check_modal.btn_small_modal.visible()
    assert check_modal.btn_large_modal.visible()

    check_modal.btn_small_modal.click()
    assert check_modal.window_small_modal.visible()
    check_modal.close_small_modal.click()
    time.sleep(1)

    check_modal.btn_large_modal.click()
    assert check_modal.window_large_modal.visible()
    check_modal.close_large_modal.click()
    time.sleep(1)


    try:
        response = requests.head(check_modal.get_url())
        if response.status_code == 200:
            assert True
    except requests.ConnectionError:
        assert False