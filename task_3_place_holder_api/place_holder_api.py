from framework.utils.api_utils import ApiUtils
from framework.utils.json_converter import JsonConverter
from task_3_place_holder_api.post import Post


class PlaceHolderApi:
    _url = 'https://jsonplaceholder.typicode.com'

    @classmethod
    def set_url(cls, base_url):
        cls._url = base_url

    @classmethod
    def _connect_to_api(cls, request, sub_url, id='', json_data=None):
        if request == 'get':
            result = ApiUtils.get_from_api(f'{cls._url}/{sub_url}/{id}')
        elif request == 'post':
            result = ApiUtils.post_to_api(f'{cls._url}/{sub_url}', json_data)
        else:
            raise Exception('Wrong request name')

        data_from_api = result.text
        post_data = JsonConverter.from_json(data_from_api)
        is_json = JsonConverter.is_json(data_from_api)
        status = result.status_code
        return post_data, is_json, status

    @classmethod
    def class_maker(cls, data, is_json, status):
        if type(data) is dict:
            if not data: data['is_empty'] = True
            data['is_json'] = is_json
            data['status'] = status
            post = Post(**data)
            return post

        elif type(data) is list:
            post_list = []
            for i in data:
                i['is_json'] = is_json
                i['status'] = status
                post = Post(**i)
                post_list.append(post)
            return post_list

    @classmethod
    def get_post(cls, id):
        return cls.class_maker(*cls._connect_to_api(request='get', sub_url='posts', id=id))

    @classmethod
    def get_posts(cls):
        return cls.class_maker(*cls._connect_to_api(request='get', sub_url='posts'))

    @classmethod
    def post_to_api(cls, data):
        return cls.class_maker(*cls._connect_to_api(request='post', sub_url='posts', json_data=data))

    @classmethod
    def get_user(cls, id):
        return cls.class_maker(*cls._connect_to_api(request='get', sub_url='users', id=id))

    @classmethod
    def get_users(cls):
        return cls.class_maker(*cls._connect_to_api(request='get', sub_url='users'))
