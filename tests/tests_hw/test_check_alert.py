# import time
# from pages.alerts import Alerts
# from selenium.webdriver.common.alert import Alert
#
#
#
# def test_check_alert(browser):
#     check_alert = Alerts(browser)
#     check_alert.visit()
#
#     assert check_alert.btn_alert.visible()
#     check_alert.btn_alert.click()
#     time.sleep(3)
#     assert not check_alert.alert()
#     time.sleep(3)
#     assert check_alert.alert()
#     check_alert.alert().accept()

from pages.alerts import Alerts
import time


def test_check_alert(browser):
    page_alert = Alerts(browser)
    page_alert.visit()

    page_alert.btn_alert.click()
    time.sleep(4)
    assert not page_alert.alert()
    time.sleep(2)
    assert page_alert.alert()
    page_alert.alert().accept()
