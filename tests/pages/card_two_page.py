from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.text_box import TextBox
from framework.elements.label import Label
from framework.elements.button import Button
from framework.elements.link import Link
from selenium.webdriver.common.keys import Keys
from framework.browser.browser import Browser
from framework.elements.dropdown import DropDown
from framework.elements.area import Area


class CardTwoPage(BasePage):
    _SEARCH_CONDITION = By.XPATH

    _INTERESTS = Area(_SEARCH_CONDITION, locator='//div[@class="avatar-and-interests__interests-list"]', name='Interests')

    def __init__(self):
        super().__init__(element=self._INTERESTS)
        self.wait_for_page_opened()
