import random
import secrets
import string


class RanGen:
    @classmethod
    def gen_rand_string(cls, length):
        return ''.join(random.choice(
            string.ascii_lowercase) for _ in range(length))

    @classmethod
    def generate_random_number_in_range(cls, a, b):
        return random.randint(a, b)

    @classmethod
    def generate_n_random_numbers_in_range(cls, n, a, b):
        answer = []
        while len(answer) < n:
            num = random.randint(a, b)
            if num not in answer:
                answer.append(num)
        return answer

    @classmethod
    def generate_password(cls, length=20):
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        return password

    @classmethod
    def generate_n_random_repeatable_numbers_in_range(cls, n, a, b):
        answer = []
        while len(answer) < n:
            num = random.randint(a, b)
            num_num = str(num) * 2
            if num_num not in answer:
                answer.append(num_num)
        return answer
