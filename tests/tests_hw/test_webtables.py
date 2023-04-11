from pages.webtables import WebTables
import allure
import time
import pytest

# @allure.title('Тест таблицы учетных записей')
# def test_webtables(browser):
#     web_tables = WebTables(browser)
#     web_tables.visit()
#     assert web_tables.btn_add
#     web_tables.btn_add.click()
#     assert web_tables.user_form.visible()
#     web_tables.btn_submit.click()
#     assert web_tables.user_form.get_dom_atribute('class') == 'was-validated'
#     web_tables.first_name.send_keys('mari')
#     web_tables.last_name.send_keys('sergeeva')
#     web_tables.email.send_keys('hdgfygf@hghgh.ru')
#     web_tables.age.send_keys('18')
#     web_tables.salary.send_keys('1000')
#     web_tables.department.send_keys('management')
#     web_tables.btn_submit.click()
#     assert web_tables.name_entry.get_text() == 'mari'
#     web_tables.pencil.click()
#     assert web_tables.user_form.visible()
#     assert web_tables.first_name.get_dom_atribute('value') == 'mari'
#     web_tables.first_name.clear()
#     web_tables.first_name.send_keys('mariya')
#     web_tables.btn_submit.click()
#     assert web_tables.name_entry.get_text() == 'mariya'
#     while web_tables.basket_delete.exist():
#         web_tables.basket_delete.click()
#     time.sleep(3)

@allure.title('')
def test_webtables(browser):
    web_tables = WebTables(browser)
    web_tables.visit()
    web_tables.number_of_line.click()
    time.sleep(3)

    assert web_tables.btn_previous.get_dom_atribute('disabled')
    assert web_tables.btn_next.get_dom_atribute('disabled')

    while web_tables.btn_next.get_dom_atribute('disabled'):
        web_tables.btn_add.click()
        web_tables.first_name.send_keys('mari')
        web_tables.last_name.send_keys('sergeeva')
        web_tables.email.send_keys('hdgfygf@hghgh.ru')
        web_tables.age.send_keys('18')
        web_tables.salary.send_keys('1000')
        web_tables.department.send_keys('management')
        time.sleep(1)
        web_tables.btn_submit.click()

    time.sleep(2)
    assert not web_tables.btn_next.get_dom_atribute('disabled')
    web_tables.btn_next.click()
    assert web_tables.number_page.get_dom_atribute('value') == '2'
    time.sleep(2)
    web_tables.btn_previous.click()
    assert web_tables.number_page.get_dom_atribute('value') == '1'
    time.sleep(2)

# @allure.title('удвление из таблицы')
# def test_webtabl(browser):
#     web_tables = WebTables(browser)
#     web_tables.visit()
#     assert not web_tables.rows_found.exist()
#     while web_tables.title_delete.exist():
#         web_tables.title_delete.click()
#     time.sleep(2)
#     assert web_tables.rows_found.exist()

