from framework.utils.api_utils import ApiUtils
from task_4_smart_vk_api.tests.test_data.test_data import TestData
from task_4_smart_vk_api.utils.response_model import ResponseModel


class VkApiUtils:
    _BASE_URL = TestData.BASE_URL
    _TOKEN = TestData.ACCESS_TOKEN_PHOTOS_WALL
    _V = TestData.API_LAST_VERSION
    _OWNER_ID = TestData.OWNER_ID

    @classmethod
    def to_response_model(cls, data):
        if 'error' in data:
            raise Exception(f'vk.com returned an error: {data}')
        elif 'response' in data:
            model_data = ResponseModel(**data['response'])
        elif 'server' in data:
            model_data = ResponseModel(**data)
        else:
            raise Exception(f'vk.com returned unknown response: {data}')
        return model_data

    @classmethod
    def result_parser(cls, result):
        if 'error' in result:
            raise Exception(f"vk.com returned an error: {result['error']}")
        else:
            return result

    @classmethod
    def create_the_post_with_text(cls, text):
        method = 'wall.post'
        params = f'owner_id={cls._OWNER_ID}&message={text}&'
        url = cls._BASE_URL.format(METHOD=method, PARAMS=params, TOKEN=cls._TOKEN, V=cls._V)
        result = ApiUtils.get_from_api(url)
        return cls.to_response_model(result)

    @classmethod
    def get_link_for_image_uploading(cls):
        method = 'photos.getWallUploadServer'
        url = cls._BASE_URL.format(METHOD=method, PARAMS='', TOKEN=cls._TOKEN, V=cls._V)
        result = ApiUtils.get_from_api(url)
        return cls.to_response_model(result).upload_url

    @classmethod
    def upload_an_image(cls, image):
        method = 'photos.saveWallPhoto'
        upload_url = cls.get_link_for_image_uploading()
        response = ApiUtils.post_to_api_multipart(upload_url, image)
        result = cls.to_response_model(response)
        params = f'photo={result.photo}&hash={result.hash}&server={result.server}&'
        url = cls._BASE_URL.format(METHOD=method, PARAMS=params, TOKEN=cls._TOKEN, V=cls._V)
        result_after_upload = ApiUtils.get_from_api(url)
        return result_after_upload['response'][0]

    @classmethod
    def add_picture_and_change_text_of_post(cls, post_id, new_text, image):
        response = cls.upload_an_image(image)
        picture_id = response['id']
        method = 'wall.edit'
        params = f'owner_id={cls._OWNER_ID}&post_id={post_id}&message={new_text}&attachments=photo{cls._OWNER_ID}_{picture_id}&'
        url = cls._BASE_URL.format(METHOD=method, PARAMS=params, TOKEN=cls._TOKEN, V=cls._V)
        result = ApiUtils.get_from_api(url)
        return cls.to_response_model(result)
