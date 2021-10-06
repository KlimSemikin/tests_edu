# coding=utf-8
from framework.elements.base.base_element import BaseElement
from framework.utils.logger import Logger


class Link(BaseElement):
    def get_href(self):
        Logger.info("Получение ссылки из элемента " + self.get_name() + " " + self.get_element_type())
        return super(Link, self).get_attribute("href")
