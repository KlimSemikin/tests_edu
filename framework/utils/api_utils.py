import requests

from framework.constants import requests_status_codes as codes
from framework.utils.json_converter import JsonConverter
from framework.utils.logger import Logger


class ApiUtils:
    @staticmethod
    def _result_parser(result, status_codes):
        if result.status_code in status_codes:
            data = JsonConverter.from_json(result.text)
            Logger.info(f"Получен ответ от API: {data}")
            return data
        else:
            raise Exception(f"Error {result.status_code} returned from API")

    @classmethod
    def get_from_api(cls, url):
        Logger.info(f"Get запрос к API {url}")
        result = requests.get(url)
        return cls._result_parser(result, (codes.OK,))

    @classmethod
    def post_to_api(cls, url, data):
        json_data = JsonConverter.to_json(data)
        Logger.info(f"Post запрос к API '{url}', {data}")
        result = requests.post(url, json_data)
        return cls._result_parser(result, (codes.OK, codes.CREATED))

    @classmethod
    def post_to_api_multipart(cls, url, files):
        Logger.info(f"Multipart post запрос к API '{url}', {files}")
        result = requests.post(url, files=files)
        return cls._result_parser(result, (codes.OK, codes.CREATED))
