from pages.webtables import WebTables
import time
from selenium.webdriver.common.by import By

def test_sort(browser):
    test_sort = WebTables(browser)
    test_sort.visit()

    column_sort = ['First Name', 'Last Name', 'Age', 'Email', 'Salary', 'Department', 'Action']

    for column in column_sort:
        browser.find_element(By.XPATH, f"// *[. = '{column}']").click()
        assert browser.find_element(By.XPATH, f"// *[. = '{column}']").get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
        time.sleep(2)
    time.sleep(2)
    browser.quit()





    # test_sort.column_first_name.click()
    # time.sleep(2)
    # assert test_sort.column_first_name.get_dom_atribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    # test_sort.column_last_name.click()
    # time.sleep(2)
    # assert test_sort.column_last_name.get_dom_atribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    # test_sort.column_age.click()
    # time.sleep(2)
    # assert test_sort.column_age.get_dom_atribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    # test_sort.column_email.click()
    # time.sleep(2)
    # assert test_sort.column_email.get_dom_atribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    # test_sort.column_salary.click()
    # time.sleep(2)
    # assert test_sort.column_salary.get_dom_atribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    # test_sort.column_department.click()
    # time.sleep(2)
    # assert test_sort.column_department.get_dom_atribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    # test_sort.column_action.click_force()
    # time.sleep(2)
    # assert test_sort.column_action.get_dom_atribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'

    #// *[. = 'Нужный мне текст']
