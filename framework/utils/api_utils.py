import requests


class ApiUtils:
    @staticmethod
    def get_from_url(url):
        return requests.get(url)

    @staticmethod
    def post_to_url(data, url):
        return requests.post(url, data)
