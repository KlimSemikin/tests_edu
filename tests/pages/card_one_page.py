from selenium.webdriver.common.by import By

from framework.elements.button import Button
from framework.elements.dropdown import DropDown
from framework.elements.label import Label
from framework.elements.text_box import TextBox
from framework.pages.base_page import BasePage


class CardOnePage(BasePage):
    _SEARCH_CONDITION = By.XPATH

    _TXB_PASSWORD = TextBox(_SEARCH_CONDITION, locator='//input[@placeholder="Choose Password"]', name='Password')

    _TXB_EMAIL = TextBox(_SEARCH_CONDITION, locator='//input[@placeholder="Your email"]', name='Email')

    _TXB_DOMAIN = TextBox(_SEARCH_CONDITION, locator='//input[@placeholder="Domain"]', name='Domain')

    _loc_domain_option = '''//div[@class="dropdown__list-item" and contains(text(),'{}')]'''

    _BTN_ACCEPT_TERMS = Button(_SEARCH_CONDITION, locator='//span[@class="checkbox__box"]', name='AcceptTerms')

    _BTN_NEXT = Button(_SEARCH_CONDITION, locator='//a[@class="button--secondary"]', name='NextButton')

    _DROPDOWN = DropDown(_SEARCH_CONDITION, locator='//div[@class="dropdown__header"]', name='DomainsList')

    _BTN_SEND_TO_BOTTOM = Button(_SEARCH_CONDITION,
                                 locator='//button[@class="button button--solid button--blue help-form__send-to-bottom-button"]',
                                 name='SendToBottom')

    _LBL_HELPER_TITLE = Label(_SEARCH_CONDITION, locator='//*[@class="help-form__title"]', name='HelperTitle')

    _BTN_NOT_REALLY_NO = Button(_SEARCH_CONDITION,
                                locator='//button[@class="button button--solid button--transparent"]',
                                name='NotReallyNot')

    _LBL_TIMER = Label(_SEARCH_CONDITION, locator='//div[@class="timer timer--white timer--center"]', name='Timer')

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
        select_domain = Button(self._SEARCH_CONDITION,
                               locator=self._loc_domain_option.format(domain_2),
                               name=f'Domain \'{domain_2}\'')
        select_domain.click()

    def accept_terms(self):
        self._BTN_ACCEPT_TERMS.click()

    def click_next_button(self):
        self._BTN_NEXT.click()

    def hide_helper(self):
        self._BTN_SEND_TO_BOTTOM.click()
        self._LBL_HELPER_TITLE.wait_for_invisibility()

    def helper_is_invisible(self):
        return self._LBL_HELPER_TITLE.is_invisible()

    def accept_cookies(self):
        self._BTN_NOT_REALLY_NO.wait_for_visibility()
        self._BTN_NOT_REALLY_NO.click()
        self._BTN_NOT_REALLY_NO.wait_for_invisibility()

    def the_form_is_disappeared(self):
        return self._BTN_NOT_REALLY_NO.is_invisible()

    def get_timer_time(self):
        return self._LBL_TIMER.get_text()
