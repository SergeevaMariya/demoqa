import time

from pages.demoqa import Demoqa
from pages.accordian import Accordian
import pytest

def test_seo(browser):
    demo_page = Demoqa(browser)
    demo_page.visit()
    assert browser.title == demo_page.pageData['title']


@pytest.mark.parametrize("pages", [Demoqa, Accordian])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert browser.title == page.pageData['title']
