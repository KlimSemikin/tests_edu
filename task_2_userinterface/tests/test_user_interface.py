import os

import task_2_userinterface.tests.test_data as td
from framework.browser.browser import Browser
from framework.utils.random_generator import RanGen
from task_2_userinterface.pages.card_one_page import CardOnePage
from task_2_userinterface.pages.card_three_page import CardThreePage
from task_2_userinterface.pages.card_two_page import CardTwoPage
from task_2_userinterface.pages.welcome_page import WelcomePage
from task_2_userinterface.sql.test_table import TestTable
from framework.utils.datetime_util import DatetimeUtil


class TestUserInterface(object):
    def test_case_1(self, create_browser, sql_report_after_test):
        Browser.get_browser().set_url(td.url)
        welcome_page = WelcomePage()
        assert welcome_page.is_opened(), 'WelcomePage не открыта'

        welcome_page.go_to_card_one_page()
        card_one_page = CardOnePage()
        assert card_one_page.is_opened(), 'CardOnePage не открыта'

        password = RanGen.generate_password()
        card_one_page.enter_pass_email_domains(password, td.email, td.domain, td.domain_2)
        card_one_page.accept_terms()
        card_one_page.click_next_button()
        card_two_page = CardTwoPage()
        assert card_two_page.is_opened(), 'CardTwoPage не открыта'

        card_two_page.click_upload_button()
        os.system(td.image_path.format(os.getcwd()[:-5]))
        card_two_page.select_three_random_interests()
        card_two_page.click_next_btn()
        card_three_page = CardThreePage()
        assert card_three_page.is_opened(), 'CardThreePage не открыта'

    def test_case_2(self, create_browser, sql_report_after_test):
        Browser.get_browser().set_url(td.url)
        welcome_page = WelcomePage()
        welcome_page.go_to_card_one_page()
        card_one_page = CardOnePage()

        card_one_page.hide_helper()
        assert card_one_page.helper_is_invisible(), 'Форма помощи не скрыта'


class TestDataBase:
    def test_db(self, pre_post_conditions_for_tc_2):
        ids = pre_post_conditions_for_tc_2
        TestTable().update_item(ids[0], column='status_id', value=2)
        TestTable().update_item(ids[1], column='start_time', value=DatetimeUtil.get_str_datetime())
        import time
        time.sleep(1)
        TestTable().update_item(ids[1], column='end_time', value=DatetimeUtil.get_str_datetime())
        TestTable().update_item(ids[2], column='browser', value='firefox')
        TestTable().update_item(ids[3], column='env', value='test_env')