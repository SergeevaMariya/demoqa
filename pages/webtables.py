from pages.base_page import BasePage
from components.components import WebElement
class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.pageData = {
            "title": "DEMOQA"
        }

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.user_form = WebElement(driver, '#userForm')
        self.btn_submit = WebElement(driver, '#submit')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.name_entry = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(1)')
        self.pencil = WebElement(driver, '#edit-record-4')
        self.new_name = WebElement(driver, '#delete-record-4')
        self.title_delete = WebElement(driver, '[title="Delete"')
        self.rows_found = WebElement(driver, 'div.rt-noData')

