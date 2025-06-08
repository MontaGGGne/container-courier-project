import random
import string


def generate_code():
    return ''.join(random.sample(string.digits, 4))

