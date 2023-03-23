from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage


def test_check_text(browser):
    demo_page = Demoqa(browser)
    demo_page.visit()
    assert demo_page.text_footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_check_please(browser):
    demo_page = Demoqa(browser)
    elments_page = ElementsPage(browser)

    demo_page.visit()
    browser.execute_script('window.scrollBy(0, 100);', '#app > div > div > div.home-body > div > div:nth-child(1)')
    demo_page.btn_elements.click()
    # elments_page.visit()
    assert elments_page.text_please.get_text() == 'Please select an item from left to start practice.'
