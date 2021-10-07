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

    _BTN_UNSELECT_ALL = Button(_SEARCH_CONDITION, locator='//label[@for="interest_unselectall"]//span[@class="checkbox__box"]', name='UnselectAll')

    _BTN_UPLOAD = Button(_SEARCH_CONDITION, locator='//a[@class="avatar-and-interests__upload-button"]', name='Upload')

    _BTNS_ALL_INTERESTS = Button(_SEARCH_CONDITION, locator="//div[@class='avatar-and-interests__interests-list__item']", name='Interests')

    _BTN_NEXT = Button(_SEARCH_CONDITION, locator='//button[@class="button button--stroked button--white button--fluid"]', name='Next')

    _LBL_AVATAR = Label(_SEARCH_CONDITION, locator='//div[@class="avatar-and-interests__avatar-image"]', name='Avatar')

    _LOC_CHECKBOX = "//span[@class='checkbox small']"

    def __init__(self):
        super().__init__(element=self._BTN_UNSELECT_ALL)
        self.wait_for_page_opened()

    def select_interests(self, numbers):
        self._BTN_UNSELECT_ALL.js_click()
        for i in numbers:
            interest = self._BTNS_ALL_INTERESTS[i]
            interest_check_box = interest(sub_locator=self._LOC_CHECKBOX, new_name_of='Interest')
            interest_check_box.click()

    def click_next_btn(self):
        self._LBL_AVATAR.wait_for_is_present()
        self._BTN_NEXT.js_click()

    def click_upload_button(self):
        self._BTN_UPLOAD.js_click()
