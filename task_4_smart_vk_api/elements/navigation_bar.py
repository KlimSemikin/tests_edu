from selenium.webdriver.common.by import By

from framework.elements.link import Link
from framework.elements.side_bar import SideBar


class NavigationBar(SideBar):
    _SEARCH_BY = By.XPATH
    _ITEMS_TYPE = Link
    _ITEMS = {'my_profile': "//li[@id='l_pr']//a"}
