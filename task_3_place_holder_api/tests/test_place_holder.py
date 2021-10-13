from task_3_place_holder_api.tests import test_data
from task_3_place_holder_api.place_holder_api import PlaceHolderApi


class TestPlaceHolder:
    def test_post_get(self):
        posts = PlaceHolderApi.get_posts()
        assert posts.status == 200, 'Статус код не 200'
        assert posts.is_json, 'Данные не являются json'
        ids_lst = [post.id for post in posts.data]
        assert ids_lst == sorted(ids_lst), 'Список не отсортирован по возрастанию'

        post_99 = PlaceHolderApi.get_post(99)
        assert post_99.status == 200, 'Статус код не 200'
        assert post_99.data.userId == 10
        assert post_99.data.id == 99
        assert post_99.data.title != ''
        assert post_99.data.body != ''

        post_150 = PlaceHolderApi.get_post(150)
        assert post_150.status == 404, 'Сатус код не 404'
        assert post_150.data

        post_to_api = PlaceHolderApi.post_to_api(test_data.post_data)
        assert post_to_api.status == 201, 'Статус код не 201'
        assert post_to_api.data.id, 'Ответ не содержит поле "id"'


        # ApiUtils.get_from_api(test_data.users)
        # assert ApiUtils.get_status_code() == 200, 'Статус код не 200'
        # assert ApiUtils.result_is_json(), 'Данные не являются json'
        # user_5_data = ApiUtils.get_result_with('id', 5)
        # assert user_5_data == test_data.user_5_data, 'Данные пользователя 5 не совпадают'
        #
        # ApiUtils.get_from_api(test_data.users + '/5')
        # assert ApiUtils.get_status_code() == 200, 'Статус код не 200'
        # assert ApiUtils.get_result() == test_data.user_5_data, 'Данные пользователя 5 не совпадают'
