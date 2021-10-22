import allure
import pytest

from framework.browser.browser import Browser
from framework.config.browser import BrowserConfig, Grid
from framework.utils.datetime_util import DatetimeUtil
from framework.utils.logger import Logger
import socket
from task_2_userinterface.sql.test_table import TestTable
from framework.constants.date_time_constants import TIMESTAMP_FORMAT_FOR_SQL
from task_2_userinterface.tests import test_data
import getpass

LOG_DATA = {}


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=BrowserConfig.BROWSER,
                     help="Name of browser")
    parser.addoption("--grid_port", action="store", default=Grid.GRID_PORT,
                     help="Port of remote connection")


@pytest.fixture(scope="function")
def create_browser(request):
    """
        Создание сессии браузера с именем из конфиг файла.
    Args:

    """
    with allure.step("Создание сессии браузера из конфиг файла"):
        browser = request.config.getoption('--browser')
        Browser.get_browser().set_up_driver(browser_key=browser, grid_port=request.config.getoption('--grid_port'))
        Browser.get_browser().maximize(browser_key=browser)

    yield

    with allure.step("Закрытие сессий всех браузеров"):
        for browser_key in list(Browser.get_browser().get_driver_names()):
            Browser.get_browser().quit(browser_key=browser_key)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        LOG_DATA['status'] = report.outcome
        LOG_DATA['start_time'] = DatetimeUtil.from_unix(call.start)
        LOG_DATA['end_time'] = DatetimeUtil.from_unix(call.stop)
        LOG_DATA['method_name'] = report.nodeid.replace('::', ' ')
        LOG_DATA['name'] = LOG_DATA['method_name'].split(' ')[1]


@pytest.fixture(scope="session", autouse=True)
def sql_session_time():
    LOG_DATA['session_start_time'] = DatetimeUtil.get_str_datetime(TIMESTAMP_FORMAT_FOR_SQL)


@pytest.fixture
def sql_report_after_test():
    yield
    LOG_DATA['env'] = socket.gethostname()
    LOG_DATA['browser'] = BrowserConfig.BROWSER
    Logger.info('Занесение результатов тестирвоания в sql базу данных')
    TestTable().add_test_record(LOG_DATA)


@pytest.fixture
def pre_post_conditions_for_tc_2():
    data_list = TestTable().get_items_with_repeatable_ids(n=4)
    ids = []
    for data in data_list:
        data['author_id'] = TestTable().get_author_id_and_add_if_needs()
        data['project_id'] = TestTable().get_project_id_and_add_if_needs()
        ids.append(str(TestTable().add_test_record(data)))
    yield ids
    TestTable().del_items(ids)