from selenium.webdriver.common.by import By

from framework.elements.link import Link
from framework.pages.base_page import BasePage


class WelcomePage(BasePage):
    _LNK_HERE = Link(By.XPATH, locator="//a[@class='start__link']", name='HERE')

    def __init__(self):
        super().__init__(element=self._LNK_HERE)
        self.wait_for_page_opened()

    def go_to_card_one_page(self):
        self._LNK_HERE.click()
