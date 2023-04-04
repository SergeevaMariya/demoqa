from pages.text_box import TextBox
import allure

@allure.feature('check attr')
@allure.story('Проверка отсутствия атрибута')
@allure.severity(allure.severity_level.BLOCKER)

def test_fail():
    assert 111 == 222

def test_placeholder(browser):
    text_box = TextBox(browser)
    text_box.visit()

    assert text_box.user_name.get_dom_atribute('placeholder') == 'Full Name'

