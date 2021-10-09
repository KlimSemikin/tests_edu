from selenium.webdriver.common.by import By

from framework.elements.text_box import TextBox
from framework.pages.base_page import BasePage


class CardThreePage(BasePage):
    _SEARCH_CONDITION = By.XPATH

    _TXB_PLACEHOLDER = TextBox(_SEARCH_CONDITION, locator='//div[@class="personal-details__td-value"]',
                               name='Placeholder')

    def __init__(self):
        super().__init__(element=self._TXB_PLACEHOLDER)
        self.wait_for_page_opened()
