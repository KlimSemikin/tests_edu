from task_3_place_holder_api.place_holder_api import PlaceHolderApi
from task_3_place_holder_api.tests import test_data


class TestPlaceHolder:
    def test_post_get(self):
        posts = PlaceHolderApi.get_posts()
        assert posts[0].status == 200, 'Статус код не 200'
        assert posts[0].is_json, 'Данные не являются json'
        ids_lst = [post.id for post in posts]
        assert ids_lst == sorted(ids_lst), 'Список не отсортирован по возрастанию'

        actual_post_99 = PlaceHolderApi.get_post(99)
        expected_post = PlaceHolderApi.class_maker(*test_data.expected_post_99)
        assert actual_post_99 == expected_post, 'Пост 99 не соответсвует ожидаемому'

        actual_post_150 = PlaceHolderApi.get_post(150)
        assert actual_post_150.status == 404
        assert actual_post_150.is_empty, 'Пост 150 пустой'

        posting_to_api = PlaceHolderApi.post_to_api(test_data.posting_data)
        assert posting_to_api.status == 201
        expected_post_data = PlaceHolderApi.class_maker(test_data.expected_post_data, True, 201)
        assert posting_to_api == expected_post_data, 'Результат постинга не соответсвует ожидаемому'
        assert 'id' in posting_to_api.__dict__, 'Ответ не содержит поле "id"'

        actual_users = PlaceHolderApi.get_users()
        assert actual_users[0].status == 200
        assert actual_users[0].is_json
        expected_user = PlaceHolderApi.class_maker(test_data.user_5_data, True, 200)
        actual_user_five = None
        for user in actual_users:
            if user.id == 5: actual_user_five = user
        assert actual_user_five == expected_user, 'Пользователь 5 не найден либо данные не соответсвуют ожидаемым'

        user_five = PlaceHolderApi.get_user(5)
        assert user_five.status == 200
        assert user_five == actual_user_five
