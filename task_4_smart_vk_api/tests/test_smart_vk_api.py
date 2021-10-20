# import os

from framework.browser.browser import Browser
from framework.utils.image_utils import ImageUtils
from framework.utils.random_generator import RanGen
from task_4_smart_vk_api.pages.feed_page import FeedPage
from task_4_smart_vk_api.pages.my_profile_page import MyProfilePage
from task_4_smart_vk_api.pages.welcome_page import WelcomePage
from task_4_smart_vk_api.tests.test_data.test_data import TestData
from task_4_smart_vk_api.utils.vk_api_utils import VkApiUtils


class TestSmartVKApi:
    def test_vk_posting(self, create_browser):
        Browser.get_browser().set_url(TestData.MAIN_URL)
        welcome_page = WelcomePage()
        assert welcome_page.is_opened()
        welcome_page.sign_in()

        feed_page = FeedPage()
        assert feed_page.is_opened()
        feed_page.menu.navigate_to('my_profile')

        my_profile_page = MyProfilePage(owner_id=TestData.OWNER_ID)
        assert my_profile_page.is_opened()

        random_text_1 = RanGen.gen_rand_string(30)
        response = VkApiUtils.create_the_post_with_text(random_text_1)
        assert my_profile_page.post_exists(post_id=response.post_id)
        actual_text = my_profile_page.get_post_text(post_id=response.post_id)
        assert random_text_1 == actual_text

        random_text_2 = RanGen.gen_rand_string(30)
        VkApiUtils.add_picture_and_change_text_of_post(post_id=response.post_id, new_text=random_text_2,
                                                       image=TestData.IMAGE)
        actual_text = my_profile_page.get_post_text(post_id=response.post_id)
        assert random_text_1 != actual_text

        img_url_from_vk = my_profile_page.get_post_image_url(post_id=response.post_id)
        Browser().back_page()
        actual_img = ImageUtils.download_the_image_from_url(img_url_from_vk)
        expected_img = TestData.IMAGE_PATH
        assert ImageUtils.image_comparator(expected_img, actual_img)

        random_text_3 = RanGen.gen_rand_string(30)
        VkApiUtils.add_comment_to_post(post_id=response.post_id, comment_text=random_text_3)
        assert my_profile_page.comment_exist(post_id=response.post_id, reply_author_id=TestData.OWNER_ID)

        my_profile_page.like_the_post(post_id=response.post_id)
        response_2 = VkApiUtils.get_post_likes(post_id=response.post_id)
        assert int(TestData.OWNER_ID) in response_2.items

        VkApiUtils.delete_the_post(post_id=response.post_id)
        assert my_profile_page.post_is_not_exist(post_id=response.post_id)
