import random
import string


class RandomGenerator:
    @classmethod
    def generate_random_string(cls, length):
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