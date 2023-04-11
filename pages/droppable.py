from components.components import WebElement
from pages.base_page import BasePage


class DropPable(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/droppable'
        super().__init__(driver, self.base_url)

        self.pageData = {
            "title": "DEMOQA"
        }
        self.drag = WebElement(driver, '#draggable')
        self.drop = WebElement(driver, '#droppable')
