from pages.form_page import FormPage
import time


def test_login_form_validate(browser):
    form_page = FormPage(browser)
    form_page.visit()
    assert form_page.first_name.get_dom_atribute('placeholder') == 'First Name'
    assert form_page.last_name.get_dom_atribute('placeholder') == 'Last Name'
    assert form_page.email.get_dom_atribute('placeholder') == 'name@example.com'
    assert form_page.email.get_dom_atribute('pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
    form_page.btn_submit.click_force()
    time.sleep(5)
    assert form_page.user_form.get_dom_atribute('class') == 'was-validated'
