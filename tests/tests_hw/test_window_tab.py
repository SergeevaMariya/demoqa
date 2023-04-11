from pages.links import Links



def test_links(browser):
    links = Links(browser)
    links.visit()

    assert links.btn_home.visible()
    assert links.btn_home.get_text() == 'Home'
    assert links.btn_home.get_dom_atribute('href') == "https://demoqa.com"
    links.btn_home.click()
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == 'https://demoqa.com/'
    assert len(browser.window_handles) == 2

