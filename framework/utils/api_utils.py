import requests

from framework.utils.logger import Logger
from framework.constants import requests_status_codes as codes
from framework.utils.json_converter import JsonConverter


class ApiUtils:
    @staticmethod
    def _result_parser(result, status):
        if result.status_code == status:
            data = JsonConverter.from_json(result.text)
            return data
        else:
            raise Exception(f"Error {result.status_code} returned from API")

    @classmethod
    def get_from_api(cls, url):
        Logger.info(f"Get запрос к API {url}")
        result = requests.get(url)
        return cls._result_parser(result, codes.OK)

    @classmethod
    def post_to_api(cls, url, data):
        json_data = JsonConverter.to_json(data)
        Logger.info(f"Post запрос к API {url}")
        result = requests.post(url, json_data)
        return cls._result_parser(result, codes.CREATED)
