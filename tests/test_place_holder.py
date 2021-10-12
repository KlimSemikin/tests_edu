from framework.api_utils import ApiUtils
from tests import test_data


class TestPlaceHolder:
    def test_posts(self, set_url):
        ApiUtils.get_from_api(test_data.sub_url_posts)
        assert ApiUtils.get_status_code() == 200, 'Статус код не 200'
        assert ApiUtils.result_is_json(), 'Данные не являются json'
        ids_lst = [i['id'] for i in ApiUtils.get_result()]
        assert ids_lst == sorted(ids_lst), 'Список не отсортирован по возрастанию'

    def test_post_99(self, set_url):
        ApiUtils.get_from_api(test_data.sub_url_posts + '/99')
        assert ApiUtils.get_status_code() == 200, 'Статус код не 200'
        result = ApiUtils.get_result()
        assert result['userId'] == 10
        assert result['id'] == 99
        assert result['title'] != ''
        assert result['body'] != ''

    def test_posting(self, set_url):
        ApiUtils.post_to_api(test_data.post_data, test_data.sub_url_posts)
        assert ApiUtils.get_status_code() == 201, 'Статус код не 201'
        assert 'id' in ApiUtils.get_result(), 'Ответ не содержит поле "id"'

    def test_users_5(self, set_url):
        ApiUtils.get_from_api(test_data.users)
        assert ApiUtils.get_status_code() == 200, 'Статус код не 200'
        assert ApiUtils.result_is_json(), 'Данные не являются json'
        user_5_data = ApiUtils.get_result_with('id', 5)
        assert user_5_data == test_data.user_5_data, 'Данные пользователя 5 не совпадают'

    def test_user_5(self, set_url):
        ApiUtils.get_from_api(test_data.users + '/5')
        assert ApiUtils.get_status_code() == 200, 'Статус код не 200'
        assert ApiUtils.get_result() == test_data.user_5_data, 'Данные пользователя 5 не совпадают'
