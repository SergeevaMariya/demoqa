import time

from pages.droppable import DropPable
from selenium.webdriver import ActionChains


def test_drag_and_drop(browser):
    page = DropPable(browser)
    action_chains = ActionChains(browser)
    page.visit()
    action_chains.drag_and_drop(page.drag.find_element(), page.drop.find_element()).perform()
    time.sleep(1)
    assert page.drop.check_css_new('backgroundColor', 'rgba(70, 130, 180, 1)')
    action_chains.drag_and_drop_by_offset(page.drop.find_element(), 100, 100).perform()
    time.sleep(2)
    assert page.drop.check_css_new('backgroundColor', 'rgba(70, 130, 180, 1)')
    time.sleep(3)