from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.text_box import TextBox
from framework.elements.label import Label
from framework.elements.button import Button
from framework.elements.link import Link
from selenium.webdriver.common.keys import Keys
from framework.browser.browser import Browser


class WelcomePage(BasePage):
    _SEARCH_CONDITION = By.XPATH

    _LNK_HERE = Link(_SEARCH_CONDITION, locator="//a[@class='start__link']", name='HERE')

    def __init__(self):
        super().__init__(element=self._LNK_HERE)
        self.wait_for_page_opened()

    def to_next_page(self):
        self._LNK_HERE.click()
