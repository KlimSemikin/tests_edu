import os

import tests.test_data as td
from framework.browser.browser import Browser
from framework.utils.random_generator import RandomGenerator
from tests.pages.card_one_page import CardOnePage
from tests.pages.card_three_page import CardThreePage
from tests.pages.card_two_page import CardTwoPage
from tests.pages.welcome_page import WelcomePage


class TestUserInterface(object):
    def test_case_1(self, create_browser):
        Browser.get_browser().set_url(td.url)
        welcome_page = WelcomePage()
        assert welcome_page.is_opened(), 'WelcomePage не открыта'

        welcome_page.go_to_card_one_page()
        card_one_page = CardOnePage()
        assert card_one_page.is_opened(), 'CardOnePage не открыта'

        password = RandomGenerator.generate_password()
        card_one_page.enter_pass_email_domains(password, td.email, td.domain, td.domain_2)
        card_one_page.accept_terms()
        card_one_page.click_next_button()
        card_two_page = CardTwoPage()
        assert card_two_page.is_opened(), 'CardTwoPage не открыта'

        card_two_page.click_upload_button()
        os.system(td.image_path.format(os.getcwd()))
        card_two_page.select_three_random_interests()
        card_two_page.click_next_btn()
        card_three_page = CardThreePage()
        assert card_three_page.is_opened(), 'CardThreePage не открыта'

    def test_case_2(self, create_browser):
        Browser.get_browser().set_url(td.url)
        welcome_page = WelcomePage()
        welcome_page.go_to_card_one_page()
        card_one_page = CardOnePage()

        card_one_page.hide_helper()
        assert card_one_page.helper_is_invisible(), 'Форма помощи не скрыта'

    def test_case_3(self, create_browser):
        Browser.get_browser().set_url(td.url)
        welcome_page = WelcomePage()
        welcome_page.go_to_card_one_page()
        card_one_page = CardOnePage()

        card_one_page.accept_cookies()
        assert card_one_page.the_form_is_disappeared(), 'Форма принятия куки не скрыта'

    def test_case_4(self, create_browser):
        Browser.get_browser().set_url(td.url)
        welcome_page = WelcomePage()
        welcome_page.go_to_card_one_page()
        card_one_page = CardOnePage()

        assert card_one_page.get_timer_time() == td.time, f'Время таймера не равно {td.time}'
