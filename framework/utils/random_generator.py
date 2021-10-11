import random
import string


class RandomGenerator:
    @classmethod
    def generate_random_string(cls, length):
        return ''.join(random.choice(
            string.ascii_lowercase) for _ in range(length))
