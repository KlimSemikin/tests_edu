from framework.utils.api_utils import ApiUtils
from framework.utils.json_converter import JsonConverter


class ApiController:
    _status_code = None
    _data = None
    _url = None

    @classmethod
    def set_url(cls, base_url):
        cls._url = base_url

    @classmethod
    def get_from_api(cls, sub_url):
        result = ApiUtils.get_from_url(cls._url + sub_url)
        cls._status_code = result.status_code
        cls._data = result.text

    @classmethod
    def post_to_api(cls, data, sub_url):
        js_data = JsonConverter.to_json(data)
        result = ApiUtils.post_to_url(js_data, str(cls._url + sub_url))
        cls._status_code = result.status_code
        cls._data = result.text

    @classmethod
    def get_status_code(cls):
        return cls._status_code

    @classmethod
    def result_is_json(cls):
        return JsonConverter.is_json(cls._data)

    @classmethod
    def get_result(cls):
        return JsonConverter.from_json(cls._data)

    @classmethod
    def get_result_with(cls, key, value):
        for i in cls.get_result():
            if i[key] == value:
                return i
