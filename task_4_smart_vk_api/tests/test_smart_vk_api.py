# import os

from task_4_smart_vk_api.tests.test_data.test_data import TestData
from task_4_smart_vk_api.pages.welcome_page import WelcomePage
from framework.browser.browser import Browser
from task_4_smart_vk_api.pages.feed_page import FeedPage
from task_4_smart_vk_api.pages.my_profile_page import MyProfilePage
from task_4_smart_vk_api.utils.vk_api_utils import VkApiUtils
from framework.utils.random_generator import RandomGenerator


class TestSmartVKApi:
    def test_vk_posting(self, create_browser):
        Browser.get_browser().set_url(TestData.MAIN_URL)
        welcome_page = WelcomePage()
        assert welcome_page.is_opened()
        welcome_page.sign_in()

        feed_page = FeedPage()
        assert feed_page.is_opened()
        feed_page.menu.navigate_to('my_profile')

        my_profile_page = MyProfilePage()
        assert my_profile_page.is_opened()

        random_text = RandomGenerator.generate_random_string(30)
        response = VkApiUtils.create_the_post_with_text(random_text)
        assert my_profile_page.post_was_added(id=TestData.OWNER_ID, number=response.post_id, expected_text=random_text)
