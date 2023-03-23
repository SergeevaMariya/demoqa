#отдельный файл, без наследования , в котором хранятся методы
import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class WebElement:

    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def get_text(self):
        return str(self.find_element().text)



    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def scroll_two_element(self):
        self.driver.execute_script('window.scrollBy(0, 100);', '#app > div > div > div.home-body > div > div:nth-child(1)')