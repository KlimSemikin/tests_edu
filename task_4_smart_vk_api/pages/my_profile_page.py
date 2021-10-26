from selenium.webdriver.common.by import By

from framework.elements.content import Content
from framework.elements.link import Link
from framework.pages.base_page import BasePage


class MyProfilePage(BasePage):
    _LNK_MY_POSTS = Link(By.XPATH, locator='//li[@class="_wall_tab_own"]//a', name='MyPosts')
    _loc_post = '//div[@data-post-id="{id}_{number}"]'
    _loc_post_text = "//div[contains(@class, 'wall_post_text')]"
    _loc_post_img = "//div[contains(@class, 'page_post_sized_thumbs')]//a"
    _CONT_OPEN_IMAGE = Content(By.XPATH, locator="//div[@id='pv_photo']//img", name='OpenImage')
    _lnk_show_comments = "//a[contains(@class, 'replies_next')]"
    _loc_post_comment = "//div[@class='replies']//div[contains(@class, 'reply')]"
    _loc_post_comment_author = "//a[@class='author']"
    _loc_like_post = "//a[contains(@class, 'like_btn')][1]"

    def __init__(self):
        super().__init__(element=self._LNK_MY_POSTS)
        self.wait_for_page_opened()
        self.owner_id = ''

    def set_owner_id(self, o_id):
        self.owner_id = o_id

    def post_exists(self, post_id):
        cont_post = Content(By.XPATH, locator=self._loc_post.format(id=self.owner_id, number=post_id), name='Post')
        return cont_post.is_displayed()

    def post_is_not_exist(self, post_id):
        cont_post = Content(By.XPATH, locator=self._loc_post.format(id=self.owner_id, number=post_id), name='Post')
        return cont_post.is_invisible()

    def get_post_text(self, post_id):
        cont_post = Content(By.XPATH, locator=self._loc_post.format(id=self.owner_id, number=post_id), name='Post')
        text = cont_post(sub_locator=self._loc_post_text, new_name_of='PostText').get_text()
        return text

    def get_post_image_url(self, post_id):
        cont_post = Content(By.XPATH, locator=self._loc_post.format(id=self.owner_id, number=post_id), name='Post')
        image = cont_post(sub_locator=self._loc_post_img, new_name_of='PostImg')
        image.click()
        img_source = self._CONT_OPEN_IMAGE.get_attribute('src')
        return img_source

    def comment_exist(self, post_id, reply_author_id=None):
        cont_post = Content(By.XPATH, locator=self._loc_post.format(id=reply_author_id or self.owner_id, number=post_id), name='Post')
        cont_post(sub_locator=self._lnk_show_comments, new_name_of='LinkShowComments').click()
        comment = cont_post(sub_locator=self._loc_post_comment, new_name_of='Comment')
        comment_author = comment(sub_locator=self._loc_post_comment_author, new_name_of='CommentAuthor')
        return comment_author.get_attribute('data-from-id') == (reply_author_id or self.owner_id)

    def like_the_post(self, post_id):
        cont_post = Content(By.XPATH, locator=self._loc_post.format(id=self.owner_id, number=post_id), name='Post')
        like_button = cont_post(sub_locator=self._loc_like_post, new_name_of='LikeButton')
        like_button.click()
