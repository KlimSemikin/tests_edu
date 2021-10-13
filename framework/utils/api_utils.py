import requests


class ApiUtils:
    @staticmethod
    def get_from_api(url):
        result = requests.get(url)
        return result

    @staticmethod
    def post_to_api(url, data):
        result = requests.post(url, data)
        return result
