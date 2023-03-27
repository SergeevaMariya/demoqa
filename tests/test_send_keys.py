from pages.form_page import FormPage
import time


def test_send_keys(browser):
    send_keys = FormPage(browser)
    send_keys.visit()
    send_keys.first_name.send_keys('Mari')
    send_keys.last_name.send_keys('Sergeeva')
    send_keys.radio_btn_male.click()
    time.sleep(1)
    send_keys.radio_btn_female.click()
    time.sleep(1)
    send_keys.radio_btn_other.click()
    time.sleep(1)
    send_keys.mobile_numder.send_keys('89112703562')
    time.sleep(5)

