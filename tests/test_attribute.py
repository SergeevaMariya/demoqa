from pages.text_box import TextBox


def test_placeholder(browser):
    text_box = TextBox(browser)
    text_box.visit()

    assert text_box.user_name.get_dom_atribute('placeholder') == 'Full Name'
