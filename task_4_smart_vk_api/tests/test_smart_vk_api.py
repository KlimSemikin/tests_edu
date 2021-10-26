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
        assert welcome_page.is_opened(), 'WelcomePage не была октрыта'
        welcome_page.sign_in(email=TestData.PHONE_OR_EMAIL, password=TestData.PASSWORD)

        feed_page = FeedPage()
        assert feed_page.is_opened(), 'FeedPage не была открыта'
        feed_page.menu.navigate_to('my_profile')

        my_profile_page = MyProfilePage()
        assert my_profile_page.is_opened(), 'MyProfilePage не была открыта'
        owner_id = Browser().get_current_url().split('id')[1]
        my_profile_page.set_owner_id(owner_id)
        VkApiUtils.set_owner_id(owner_id)

        random_text_1 = RanGen.gen_rand_string(30)
        response = VkApiUtils.create_the_post_with_text(random_text_1)
        assert my_profile_page.post_exists(post_id=response.post_id), f'Пост - {response.post_id} на странице не существует'
        actual_text = my_profile_page.get_post_text(post_id=response.post_id)
        assert random_text_1 == actual_text, 'Текст поста не совпадает с ожидаемым'

        random_text_2 = RanGen.gen_rand_string(30)
        VkApiUtils.add_picture_and_change_text_of_post(post_id=response.post_id, new_text=random_text_2,
                                                       image=TestData.IMAGE)
        actual_text = my_profile_page.get_post_text(post_id=response.post_id)
        assert random_text_1 != actual_text, 'Текст поста не изменился'

        img_url_from_vk = my_profile_page.get_post_image_url(post_id=response.post_id)
        Browser().back_page()
        actual_img = ImageUtils.download_the_image_from_url(img_url_from_vk)
        expected_img = TestData.IMAGE_PATH
        assert ImageUtils.image_comparator(expected_img, actual_img), 'Загруженная и полученная картинки не совпадают'

        random_text_3 = RanGen.gen_rand_string(30)
        VkApiUtils.add_comment_to_post(post_id=response.post_id, comment_text=random_text_3)
        assert my_profile_page.comment_exist(post_id=response.post_id), 'Не существует такого комментария'

        my_profile_page.like_the_post(post_id=response.post_id)
        response_2 = VkApiUtils.get_post_likes(post_id=response.post_id)
        assert int(owner_id) in response_2.items, 'Этого id нет в списке лайкнувших'

        VkApiUtils.delete_the_post(post_id=response.post_id)
        assert my_profile_page.post_is_not_exist(post_id=response.post_id), 'Пост не был удалён'
