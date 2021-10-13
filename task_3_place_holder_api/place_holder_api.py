from framework.utils.api_utils import ApiUtils
from framework.utils.json_converter import JsonConverter


class PlaceHolderApi:
    _url = 'https://jsonplaceholder.typicode.com'

    @classmethod
    def set_url(cls, base_url):
        cls._url = base_url

    @classmethod
    def _connect_to_api(cls, request, id='', json_data=None):
        if request == 'get':
            result = ApiUtils.get_from_api(f'{cls._url}/posts/{id}')
        elif request == 'post':
            result = ApiUtils.post_to_api(f'{cls._url}/posts', json_data)
        else:
            raise Exception('Wrong request name')

        data_from_api = result.text
        is_json = JsonConverter.is_json(data_from_api)
        status = result.status_code
        return status, is_json, data_from_api

    @classmethod
    def _make_dict_from_data(cls, status, is_json, data_from_api):
        post_dict = {
            'status': status,
            'is_json': is_json,
        }

        if is_json:
            data = JsonConverter.from_json(data_from_api)
            if type(data) is dict:
                post_dict['data'] = type('Post', (), data)()
            elif type(data) is list:
                post_dict['data'] = [type('Post', (), post)() for post in data]
        return post_dict

    @classmethod
    def get_post(cls, id):
        data = cls._connect_to_api(request='get', id=id)
        dic = cls._make_dict_from_data(*data)
        return type('Post', (), dic)()

    @classmethod
    def get_posts(cls):
        data = cls._connect_to_api(request='get')
        dic = cls._make_dict_from_data(*data)
        return type('Posts', (), dic)()

    @classmethod
    def post_to_api(cls, data):
        json_data = JsonConverter.to_json(data)
        answer = cls._connect_to_api(request='post', json_data=json_data)
        dic = cls._make_dict_from_data(*answer)
        return type('Posts', (), dic)()
