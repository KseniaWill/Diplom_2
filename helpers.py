import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def create_user_data():
    user_data = {
        "email": f'{generate_random_string(5)}@yandex.ru',
        "password": generate_random_string(5),
        "name": generate_random_string(5)
        }
    return user_data
