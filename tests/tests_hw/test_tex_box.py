from pages.text_box import TextBox
import time


def test_text_box(browser):
    name = 'Mariya'
    adress = 'adress'
    text_box = TextBox(browser)
    text_box.visit()
    text_box.user_name.send_keys(name)
    text_box.current_address.send_keys(adress)
    text_box.submit.click_force()
    time.sleep(5)
    assert text_box.received_name.get_text() == f'Name:{name}'
    assert text_box.received_address.get_text() == f'Current Address :{adress}'