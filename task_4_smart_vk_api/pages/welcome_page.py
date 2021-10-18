from selenium.webdriver.common.by import By

from framework.elements.text_box import TextBox
from framework.pages.base_page import BasePage
from task_4_smart_vk_api.tests.test_data.test_data import TestData


class WelcomePage(BasePage):
    _TXB_EMAIL_OR_PHONE = TextBox(By.XPATH, locator="//input[@id='index_email']", name='PhoneEmail')
    _TXB_PASSWORD = TextBox(By.XPATH, locator="//input[@id='index_pass']", name='Password')
    _BTN_SIGN_IN = TextBox(By.XPATH, locator="//button[@id='index_login_button']", name='SignIn')

    def __init__(self):
        super().__init__(element=self._TXB_EMAIL_OR_PHONE)
        self.wait_for_page_opened()

    def enter_email_or_phone(self):
        self._TXB_EMAIL_OR_PHONE.send_keys(TestData.PHONE_OR_EMAIL)

    def enter_password(self):
        self._TXB_PASSWORD.send_keys(TestData.PASSWORD)

    def click_sign_in_button(self):
        self._BTN_SIGN_IN.click()

    def sign_in(self):
        self.enter_email_or_phone()
        self.enter_password()
        self.click_sign_in_button()
