from selenium.webdriver.common.by import By

from framework.elements.button import Button
from framework.elements.checkbox import Checkbox
from framework.elements.content import Content
from framework.elements.dropdown import DropDown
from framework.elements.text_box import TextBox
from framework.pages.base_page import BasePage


class CardOnePage(BasePage):
    _TXB_PASSWORD = TextBox(By.XPATH, locator='//input[@placeholder="Choose Password"]', name='Password')

    _TXB_EMAIL = TextBox(By.XPATH, locator='//input[@placeholder="Your email"]', name='Email')

    _TXB_DOMAIN = TextBox(By.XPATH, locator='//input[@placeholder="Domain"]', name='Domain')

    _loc_domain_option = '''//div[@class="dropdown__list-item" and contains(text(),'{}')]'''

    _CB_ACCEPT_TERMS = Checkbox(By.XPATH, locator='//span[@class="checkbox__box"]', name='AcceptTerms')

    _BTN_NEXT = Button(By.XPATH, locator='//a[@class="button--secondary"]', name='NextButton')

    _DROPDOWN = DropDown(By.XPATH, locator='//div[@class="dropdown__header"]', name='DomainsList')

    _BTN_SEND_TO_BOTTOM = Button(By.XPATH, locator='//button[contains(@class, "help-form__send-to-bottom-button")]',
                                 name='SendToBottom')

    _CONT_HELPER_TITLE = Content(By.XPATH, locator='//*[@class="help-form__title"]', name='HelperTitle')

    _BTN_NOT_REALLY_NO = Button(By.XPATH, locator='//button[@name="button" and contains(text(), "Not really, no")]',
                                name='NotReallyNo')

    _CONT_TIMER = Content(By.XPATH, locator='//div[contains(@class, "timer--white")]', name='Timer')

    def __init__(self):
        super().__init__(element=self._TXB_PASSWORD)
        self.wait_for_page_opened()

    def enter_pass_email_domains(self, password, email, domain, domain_2):
        self._TXB_PASSWORD.clear_field()
        self._TXB_PASSWORD.send_keys(password)
        self._TXB_EMAIL.clear_field()
        self._TXB_EMAIL.send_keys(email)
        self._TXB_DOMAIN.clear_field()
        self._TXB_DOMAIN.send_keys(domain)
        self._DROPDOWN.click()
        select_domain = Button(By.XPATH,
                               locator=self._loc_domain_option.format(domain_2),
                               name=f'Domain \'{domain_2}\'')
        select_domain.click()

    def accept_terms(self):
        self._CB_ACCEPT_TERMS.click()

    def click_next_button(self):
        self._BTN_NEXT.click()

    def hide_helper(self):
        self._BTN_SEND_TO_BOTTOM.click()
        self._CONT_HELPER_TITLE.wait_for_invisibility()

    def helper_is_invisible(self):
        return self._CONT_HELPER_TITLE.is_invisible()

    def accept_cookies(self):
        self._BTN_NOT_REALLY_NO.wait_for_visibility()
        self._BTN_NOT_REALLY_NO.click()
        self._BTN_NOT_REALLY_NO.wait_for_invisibility()

    def the_form_is_disappeared(self):
        return self._BTN_NOT_REALLY_NO.is_invisible()

    def get_timer_time(self):
        return self._CONT_TIMER.get_text()
