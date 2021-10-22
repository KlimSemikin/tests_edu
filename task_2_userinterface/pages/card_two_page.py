from selenium.webdriver.common.by import By

from framework.elements.button import Button
from framework.elements.checkbox import Checkbox
from framework.elements.content import Content
from framework.pages.base_page import BasePage
from framework.utils.random_generator import RanGen


class CardTwoPage(BasePage):
    _CB_UNSELECT_ALL = Checkbox(By.XPATH, locator='//label[@for="interest_unselectall"]//span[@class="checkbox__box"]',
                                name='UnselectAll')

    _BTN_UPLOAD = Button(By.XPATH, locator='//a[@class="avatar-and-interests__upload-button"]', name='Upload')

    _CBS_ALL_INTERESTS = Checkbox(By.XPATH, locator="//div[@class='avatar-and-interests__interests-list__item']",
                                  name='Interests')

    _BTN_NEXT = Button(By.XPATH, locator='//button[@name="button" and contains(text(), "Next")]', name='Next')

    _CONT_AVATAR = Content(By.XPATH, locator='//div[@class="avatar-and-interests__avatar-image"]', name='Avatar')

    _LOC_CHECKBOX = '//span[@class="checkbox__box"]'

    def __init__(self):
        super().__init__(element=self._BTN_UPLOAD)
        self.wait_for_page_opened()

    def select_three_random_interests(self):
        self._CB_UNSELECT_ALL.click()
        for i in RanGen.generate_n_random_numbers_in_range(n=3, a=1, b=20):
            interest = self._CBS_ALL_INTERESTS[i]
            interest_check_box = interest(sub_locator=self._LOC_CHECKBOX, new_name_of=f'Interest number {i}')
            interest_check_box.click()

    def click_next_btn(self):
        self._CONT_AVATAR.wait_for_is_present()
        self._BTN_NEXT.click()

    def click_upload_button(self):
        self._BTN_UPLOAD.click()
