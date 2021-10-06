from abc import ABC

from framework.browser.browser import Browser
from framework.utils.logger import Logger


class BasePage(ABC):
    def __init__(self, element):
        self._base_element = element
        self._page_name = self.__class__.__name__

    def wait_page_to_load(self):
        Logger.info("Ожидание загрузки страницы " + self._page_name + " с помощью js")
        Browser.get_browser().wait_for_page_to_load()

    def is_opened(self):
        Logger.info("Проверка, открыта ли страница " + self._page_name)
        self.wait_page_to_load()
        return Browser.get_browser().is_wait_successful(self._base_element.wait_for_is_visible)

    def wait_for_page_closed(self):
        self.wait_page_to_load()
        return Browser.get_browser().is_wait_successful(self._base_element.wait_for_is_absent)

    def wait_for_page_opened(self):
        Logger.info("Ожидание загрузки страницы " + self._page_name + " и видимости идентифицирующего ее элемента")
        self.wait_page_to_load()
        self._base_element.wait_for_is_visible()

    def refresh_page(self):
        Logger.info("Обновление страницы " + self._page_name)
        Browser.get_browser().refresh_page()
