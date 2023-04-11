from pages.demoqa import Demoqa
from pages.accordian import Accordian
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab

import pytest
import time


@pytest.mark.parametrize("pages", [Demoqa, Accordian, Alerts, BrowserTab])
def test_seo_meta(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.metaView.exist()
    assert page.metaView.get_dom_atribute('name') == "viewport"
    assert page.metaView.get_dom_atribute('content') == "width=device-width,initial-scale=1"




