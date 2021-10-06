import requests

from framework.utils.logger import Logger


class ApiUtils:
    @staticmethod
    def get_from_api(url):
        result = requests.get(url)
        Logger.info(f"Получен ответ от API {result.status_code}")
        return result

    @staticmethod
    def post_to_api(url, data):
        result = requests.post(url, data)
        Logger.info(f"Получен ответ от API {result.status_code}")
        return result
