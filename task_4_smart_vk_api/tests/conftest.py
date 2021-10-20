import allure
import pytest

from framework.browser.browser import Browser
from framework.config.browser import BrowserConfig, Grid


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=BrowserConfig.BROWSER,
                     help="Name of browser")
    parser.addoption("--grid_port", action="store", default=Grid.GRID_PORT,
                     help="Port of remote connection")
    parser.addoption("--lang", action="store", default=BrowserConfig.LOCALE,
                     help="Browser language")


@pytest.fixture(scope="function")
def create_browser(request):
    """
        Создание сессии браузера с именем из конфиг файла.
    Args:

    """
    with allure.step("Создание сессии браузера из конфиг файла"):
        browser = request.config.getoption('--browser')
        grid_port = request.config.getoption('--grid_port')
        language = request.config.getoption('--lang')
        Browser.get_browser().set_up_driver(browser_key=browser, grid_port=grid_port, lang=language)
        Browser.get_browser().maximize(browser_key=browser)

    yield

    with allure.step("Закрытие сессий всех браузеров"):
        for browser_key in list(Browser.get_browser().get_driver_names()):
            Browser.get_browser().quit(browser_key=browser_key)
