from framework.browser.browser import Browser
from tests.pages.welcome_page import WelcomePage
from tests.pages.card_one_page import CardOnePage
from tests.pages.card_two_page import CardTwoPage
import allure


class TestFunctional(object):
    def test_framework(self, create_browser):
        with allure.step("First step"):
            Browser.get_browser().set_url('https://userinyerface.com/game.html%20target=')
            welcome_page = WelcomePage()
            assert welcome_page.is_opened()

            welcome_page.to_next_page()
            card_one_page = CardOnePage()
            assert card_one_page.is_opened()

            password = 'Qwerty1234'
            email = 'qwerty1'
            domain = 'gmail'
            domain_2 = '.com'
            card_one_page.login(password, email, domain, domain_2)
            card_two_page = CardTwoPage()
            assert card_two_page.is_opened()
