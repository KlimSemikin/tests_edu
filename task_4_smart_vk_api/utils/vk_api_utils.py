from framework.utils.api_utils import ApiUtils
from task_4_smart_vk_api.tests.test_data.test_data import TestData
from task_4_smart_vk_api.utils.response_model import ResponseModel


class VkApiUtils:
    _BASE_URL = TestData.BASE_URL
    _TOKEN = TestData.ACCESS_TOKEN_PHOTOS_WALL
    _V = TestData.API_LAST_VERSION
    _OWNER_ID = TestData.OWNER_ID

    @classmethod
    def to_response_model(cls, response):
        if type(response) is dict:
            return ResponseModel(**response)
        elif type(response) is list:
            return [ResponseModel(**i) for i in response]
        raise Exception(f'vk.com returned unknown response: {response}')

    @classmethod
    def _error_checker(cls, response):
        if 'error' in response:
            raise Exception(f"vk.com returned an error: {response['error']}")
        elif 'response' in response and type(response['response']) in (dict, list):
            return response['response']
        return response

    @classmethod
    def _request_to_vk(cls, api_method, method=None, params=None, url=None, data=None):
        url = url or cls._BASE_URL.format(METHOD=method, PARAMS=params, TOKEN=cls._TOKEN, V=cls._V)
        if data:
            return cls._error_checker(api_method(url, data))
        return cls._error_checker(api_method(url))

    @classmethod
    def create_the_post_with_text(cls, text):
        method = 'wall.post'
        params = f'owner_id={cls._OWNER_ID}&message={text}&'
        result = cls._request_to_vk(ApiUtils.get_from_api, method, params)
        return cls.to_response_model(result)

    @classmethod
    def _get_link_for_image_uploading(cls):
        method = 'photos.getWallUploadServer'
        params = ''
        result = cls._request_to_vk(ApiUtils.get_from_api, method, params)
        return result['upload_url']

    @classmethod
    def upload_an_image(cls, image):
        upload_url = cls._get_link_for_image_uploading()
        upl_res = cls._request_to_vk(ApiUtils.post_to_api_multipart, url=upload_url, data=image)  # upload

        method = 'photos.saveWallPhoto'
        params = f"photo={upl_res['photo']}&hash={upl_res['hash']}&server={upl_res['server']}&"
        result = cls._request_to_vk(ApiUtils.get_from_api, method, params)
        return result[0]

    @classmethod
    def add_picture_and_change_text_of_post(cls, post_id, new_text, image):
        method = 'wall.edit'
        result_after_upload = cls.upload_an_image(image)
        picture_id = result_after_upload['id']
        params = f'owner_id={cls._OWNER_ID}&post_id={post_id}&message={new_text}&attachments=photo{cls._OWNER_ID}_{picture_id}&'
        result = cls._request_to_vk(ApiUtils.get_from_api, method, params)
        return result

    @classmethod
    def add_comment_to_post(cls, post_id, comment_text):
        method = 'wall.createComment'
        params = f'owner_id={cls._OWNER_ID}&post_id={post_id}&message={comment_text}&'
        result = cls._request_to_vk(ApiUtils.get_from_api, method, params)
        return cls.to_response_model(result)

    @classmethod
    def get_post_likes(cls, post_id):
        method = 'likes.getList'
        params = f'owner_id={cls._OWNER_ID}&item_id={post_id}&type=post&'
        result = cls._request_to_vk(ApiUtils.get_from_api, method, params)
        return cls.to_response_model(result)

    @classmethod
    def delete_the_post(cls, post_id):
        method = 'wall.delete'
        params = f'owner_id={cls._OWNER_ID}&post_id={post_id}&type=post&'
        result = cls._request_to_vk(ApiUtils.get_from_api, method, params)
        return cls.to_response_model(result)
