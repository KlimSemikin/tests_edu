from selenium.webdriver.common.by import By

from framework.pages.base_page import BasePage
from task_4_smart_vk_api.elements.navigation_bar import NavigationBar


class FeedPage(BasePage):
    menu = NavigationBar(By.XPATH, locator="//nav[@class='side_bar_nav']", name='VkMenu')

    def __init__(self):
        super().__init__(element=self.menu)
        self.wait_for_page_opened()
