# coding=utf-8
from selenium.webdriver.common.keys import Keys

from framework.elements.base.base_element import BaseElement
from framework.utils.logger import Logger


class TextBox(BaseElement):
    def get_value(self):
        self.wait_for_is_present()
        value = super(TextBox, self).get_attribute("value")
        Logger.info("Метод get_value в элементе " + self.get_name() + " " + self.get_element_type() +
                    " получил значение: " + str(value))
        return value

    def clear_field(self):
        Logger.info("Удание текста в элементе " + self.get_name() + self.get_element_type() + "'" +
                    self.get_name() + "'")
        self.send_keys(Keys.CONTROL + 'a')
        self.send_keys_without_click(Keys.DELETE)

    def selenium_clear(self):
        self.click()
        Logger.info("Очистка элемента " + self.get_name() + self.get_element_type() + "'" + self.get_name() + "'")
        self.find_element().clear()
