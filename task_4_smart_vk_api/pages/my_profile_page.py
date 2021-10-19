from selenium.webdriver.common.by import By

from framework.elements.link import Link
from framework.elements.text_box import TextBox
from framework.pages.base_page import BasePage
from task_4_smart_vk_api.tests.test_data.test_data import TestData
from framework.elements.side_bar import SideBar
from task_4_smart_vk_api.elements.navigation_bar import NavigationBar
from framework.elements.content import Content


class MyProfilePage(BasePage):
    _LNK_MY_POSTS = Link(By.XPATH, locator='//li[@class="_wall_tab_own"]//a', name='MyPosts')
    _loc_post = '//div[@data-post-id="{id}_{number}"]'
    _loc_post_text = "//div[contains(@class, 'wall_post_text')]"

    def __init__(self):
        super().__init__(element=self._LNK_MY_POSTS)
        self.wait_for_page_opened()

    def post_exists(self, id, post_id):
        cont_post = Content(By.XPATH, locator=self._loc_post.format(id=id, number=post_id), name='Post')
        return cont_post.is_displayed()

    def get_post_text(self, id, post_id):
        cont_post = Content(By.XPATH, locator=self._loc_post.format(id=id, number=post_id), name='Post')
        text = cont_post(sub_locator=self._loc_post_text, new_name_of='PostText').get_text()
        return text

    def get_post_image(self, id, post_id):
        pass
