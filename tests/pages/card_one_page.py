from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.text_box import TextBox
from framework.elements.label import Label
from framework.elements.button import Button
from framework.elements.link import Link
from selenium.webdriver.common.keys import Keys
from framework.browser.browser import Browser
from framework.elements.dropdown import DropDown


class CardOnePage(BasePage):
    _SEARCH_CONDITION = By.XPATH

    _TXB_PASSWORD = TextBox(_SEARCH_CONDITION, locator='//input[@placeholder="Choose Password"]', name='Password')

    _TXB_EMAIL = TextBox(_SEARCH_CONDITION, locator='//input[@placeholder="Your email"]', name='Email')

    _TXB_DOMAIN = TextBox(_SEARCH_CONDITION, locator='//input[@placeholder="Domain"]', name='Domain')

    _BTN_ACCEPT_TERMS = Button(_SEARCH_CONDITION, locator='//span[@class="checkbox__box"]', name='AcceptTerms')

    _BTN_NEXT = Button(_SEARCH_CONDITION, locator='//a[@class="button--secondary"]', name='NextButton')

    _DROPDOWN = DropDown(_SEARCH_CONDITION, locator='//div[@class="dropdown__header"]', name='DomainsList')

    def __init__(self):
        super().__init__(element=self._TXB_PASSWORD)
        self.wait_for_page_opened()

    def login(self, password, email, domain, domain_2):
        self._TXB_PASSWORD.clear_field()
        self._TXB_PASSWORD.send_keys(password)
        self._TXB_EMAIL.clear_field()
        self._TXB_EMAIL.send_keys(email)
        self._TXB_DOMAIN.clear_field()
        self._TXB_DOMAIN.send_keys(domain)
        self._DROPDOWN.click()
        select_domain = Button(self._SEARCH_CONDITION,
                               locator=f'''//div[@class="dropdown__list-item" and contains(text(),'{domain_2}')]''',
                               name='NextButton')
        select_domain.click()
        self._BTN_ACCEPT_TERMS.click()
        self._BTN_NEXT.click()
