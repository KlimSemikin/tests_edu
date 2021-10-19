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
        if 'response' in response:
            if type(response['response']) is dict:
                return ResponseModel(**response['response'])
            elif type(response['response']) is list:
                return [ResponseModel(**i) for i in response['response']]
        else:
            return ResponseModel(**response)
        # raise Exception(f'vk.com returned unknown response: {response}')

    @classmethod
    def _error_checker(cls, response):
        if 'error' in response:
            raise Exception(f"vk.com returned an error: {response['error']}")
        elif 'response' in response:
            return response['response']
        return response

    @classmethod
    def create_the_post_with_text(cls, text):
        method = 'wall.post'
        params = f'owner_id={cls._OWNER_ID}&message={text}&'
        url = cls._BASE_URL.format(METHOD=method, PARAMS=params, TOKEN=cls._TOKEN, V=cls._V)
        result = cls._error_checker(ApiUtils.get_from_api(url))
        return cls.to_response_model(result)

    @classmethod
    def _get_link_for_image_uploading(cls):
        method = 'photos.getWallUploadServer'
        url = cls._BASE_URL.format(METHOD=method, PARAMS='', TOKEN=cls._TOKEN, V=cls._V)
        result = cls._error_checker(ApiUtils.get_from_api(url))
        return result['upload_url']

    @classmethod
    def upload_an_image(cls, image):
        method = 'photos.saveWallPhoto'
        upload_url = cls._get_link_for_image_uploading()
        result = cls._error_checker(ApiUtils.post_to_api_multipart(upload_url, image))  # upload

        params = f"photo={result['photo']}&hash={result['hash']}&server={result['server']}&"
        url = cls._BASE_URL.format(METHOD=method, PARAMS=params, TOKEN=cls._TOKEN, V=cls._V)
        result_after_upload = cls._error_checker(ApiUtils.get_from_api(url))
        return result_after_upload[0]

    @classmethod
    def add_picture_and_change_text_of_post(cls, post_id, new_text, image):
        method = 'wall.edit'
        result_after_upload = cls.upload_an_image(image)
        picture_id = result_after_upload['id']
        params = f'owner_id={cls._OWNER_ID}&post_id={post_id}&message={new_text}&attachments=photo{cls._OWNER_ID}_{picture_id}&'
        url = cls._BASE_URL.format(METHOD=method, PARAMS=params, TOKEN=cls._TOKEN, V=cls._V)
        cls._error_checker(ApiUtils.get_from_api(url))
