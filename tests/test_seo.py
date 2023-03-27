from pages.demoqa import Demoqa


def test_seo(browser):
    demo_page = Demoqa(browser)
    demo_page.visit()
    assert browser.title == demo_page.pageData['title']
