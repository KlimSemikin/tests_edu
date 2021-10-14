from framework.utils.random_generator import RandomGenerator as RandGen

base_url = 'https://jsonplaceholder.typicode.com'
sub_url_posts = '/posts'

expected_post_99 = ({
                        'userId': 10,
                        'id': 99,
                        'title': 'temporibus sit alias delectus eligendi possimus magni',
                        'body': 'quo deleniti praesentium dicta non quod\naut est molestias\nmolestias et officia quis nihil\nitaque dolorem quia'
                    }, True, 200)

posting_data = {
    "title": RandGen.generate_random_string(8),
    "body": RandGen.generate_random_string(8),
    "userId": '1'
}

expected_post_data = {
    "title": posting_data['title'],
    "body": posting_data['body'],
    "userId": '1',
    'id': 101
}

users = '/users'
user_5_data = {
    'id': 5,
    'name': 'Chelsey Dietrich',
    'username': 'Kamren',
    'email': 'Lucio_Hettinger@annie.ca',
    'address': {
        'street': 'Skiles Walks',
        'suite': 'Suite 351',
        'city': 'Roscoeview',
        'zipcode': '33263',
        'geo': {
            'lat': '-31.8129',
            'lng': '62.5342'
        }
    },
    'phone':
        '(254)954-1289',
    'website': 'demarco.info',
    'company': {
        'name': 'Keebler LLC',
        'catchPhrase': 'User-centric fault-tolerant solution',
        'bs': 'revolutionize end-to-end systems'
    }
}
