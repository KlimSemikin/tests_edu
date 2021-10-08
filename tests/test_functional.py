from framework.browser.browser import Browser
from tests.pages.welcome_page import WelcomePage
from tests.pages.card_one_page import CardOnePage
from tests.pages.card_two_page import CardTwoPage
from tests.pages.card_three_page import CardThreePage
from framework.utils.random_generator import RandomGenerator
import os
import allure


class TestFunctional(object):
    def test_case_1(self, create_browser):
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

            nums = RandomGenerator.generate_n_random_numbers_in_range(3, 1, 20)
            card_two_page.select_interests(nums)
            card_two_page.click_upload_button()
            os.system(f"{os.getcwd()}/tools/upload_image_script.exe")
            card_two_page.click_next_btn()
            card_three_page = CardThreePage()
            assert card_three_page.is_opened()

    def test_case_2(self, create_browser):
        Browser.get_browser().set_url('https://userinyerface.com/game.html%20target=')
        welcome_page = WelcomePage()
        assert welcome_page.is_opened()

        welcome_page.to_next_page()
        card_one_page = CardOnePage()
        assert card_one_page.is_opened()

        card_one_page.hide_helper()
        assert card_one_page.helper_is_invisible()

    def test_case_3(self, create_browser):
        pass

    def test_case_4(self, create_browser):
        pass
