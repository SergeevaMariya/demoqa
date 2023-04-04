from pages.base_page import BasePage
from components.components import WebElement


class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.pageData = {
            "title": "DEMOQA"
        }

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.radio_btn_male = WebElement(driver, '#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label')
        self.radio_btn_female = WebElement(driver, '#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(2) > label')
        self.radio_btn_other = WebElement(driver, '#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(3) > label')
        self.mobile_numder = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement(driver, '#closeLargeModal')

        self.hobbies = WebElement(driver, '#hobbies-checkbox-1')
        self.current_address = WebElement(driver, '#currentAddress')
        self.user_form = WebElement(driver, '#userForm')
        self.state = WebElement(driver, '#state > div > div.css-1wy0on6')
        self.state1 = WebElement(driver, '#state > div > div.css-1hwfws3 > div.css-1uccc91-singleValue')