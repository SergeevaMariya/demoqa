from pages.slider import Slider
import time
from selenium.webdriver import ActionChains




def test_slider(browser):
    slider = Slider(browser)
    slider.visit()
    action_chains = ActionChains(browser)
    slider.slider_container.visible()
    assert slider.value_slider.get_dom_atribute('value') == '25'

    action_chains.click_and_hold(slider.value_slider.find_element()).move_by_offset(1, 0).release().perform()
    assert slider.value_slider.get_dom_atribute('value') == '50'
    time.sleep(2)
