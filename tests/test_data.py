from framework.utils.random_generator import RandomGenerator as RandGen

base_url = 'https://jsonplaceholder.typicode.com'
sub_url_posts = '/posts'
post_data = {
    "title": RandGen.generate_random_string(8),
    "body": RandGen.generate_random_string(8),
    "userId": 1
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
