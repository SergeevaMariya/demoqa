from pages.form_page import FormPage
import time


def test_send_keys(browser):
    send_keys = FormPage(browser)
    send_keys.visit()
    assert not send_keys.modal_dialog.exist()
    time.sleep(2)
    send_keys.first_name.send_keys('Mari')
    send_keys.last_name.send_keys('Sergeeva')
    send_keys.email.send_keys('mozhno_est@mail.ru')
    send_keys.radio_btn_male.click_force()
    send_keys.mobile_numder.send_keys('89112703562')
    send_keys.btn_submit.click_force()
    time.sleep(5)
    assert send_keys.modal_dialog.exist()
    send_keys.btn_close_modal.click_force()
    time.sleep(2)

