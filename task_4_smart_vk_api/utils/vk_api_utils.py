from framework.utils.api_utils import ApiUtils
from task_4_smart_vk_api.tests.test_data.test_data import TestData
from task_4_smart_vk_api.utils.response_model import ResponseModel


class VkApiUtils:
    _BASE_URL = TestData.BASE_URL
    _TOKEN = TestData.ACCESS_TOKEN
    _V = TestData.API_LAST_VERSION
    _OWNER_ID = TestData.OWNER_ID

    @classmethod
    def result_parser(cls, data):
        if 'response' in data:
            response = ResponseModel(**data['response'])
            return response
        else:
            raise Exception('vk.com returned an error')

    @classmethod
    def create_the_post_with_text(cls, text):
        method = 'wall.post'
        params = f'owner_id={cls._OWNER_ID}&message={text}'
        url = cls._BASE_URL.format(METHOD=method, PARAMS=params, TOKEN=cls._TOKEN, V=cls._V)
        result = ApiUtils.get_from_api(url)
        return cls.result_parser(result)
