from framework.elements.base.base_element import BaseElement
from framework.utils.logger import Logger


class SideBar(BaseElement):
    _SEARCH_BY = None
    _ITEMS_TYPE = None
    _ITEMS = {}

    def navigate_to(self, item):
        Logger.info(f"Переход на пункт меню '{item}' в элементе {self.get_name()} {self.get_element_type()}")
        if item in self._ITEMS:
            menu_item = self._ITEMS_TYPE(self._SEARCH_BY, locator=self.get_locator() + self._ITEMS[item], name=item)
        else:
            raise Exception('Wrong item name')
        menu_item.click()
