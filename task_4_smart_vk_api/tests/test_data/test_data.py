import os


class TestData:
    MAIN_URL = 'https://vk.com/'
    PHONE_OR_EMAIL = ''  # please enter it
    PASSWORD = ''  # please enter it
    ACCESS_TOKEN_PHOTOS_WALL = ''  # please enter it
    API_LAST_VERSION = '5.131'
    BASE_URL = 'https://api.vk.com/method/{METHOD}?{PARAMS}&access_token={TOKEN}&v={V}'
    IMAGE = {'photo': open(r'test_data/test_picture.jpg', 'rb')}
    IMAGE_PATH = os.path.abspath(f'test_data\\test_picture.jpg')
