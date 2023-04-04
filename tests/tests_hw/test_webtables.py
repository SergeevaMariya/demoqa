from pages.webtables import WebTables
import allure
import time

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
#     assert web_tables.name_entry.get_text() == 'mari'


@allure.title('удвление из таблицы')
def test_webtabl(browser):
    web_tables = WebTables(browser)
    web_tables.visit()
    assert not web_tables.rows_found.exist()
    while web_tables.title_delete.exist():
        web_tables.title_delete.click()
    time.sleep(2)
    assert web_tables.rows_found.exist()









