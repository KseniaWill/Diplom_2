class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    REGISTER_URL = BASE_URL + 'api/auth/register'
    LOGIN_URL = BASE_URL + 'api/auth/login'
    USER_URL = BASE_URL + 'api/auth/user'
    ORDERS_URL = BASE_URL + 'api/orders'


class Response:
    user_auth_error = 'email or password are incorrect'
    exist_user_error = 'User already exists'
    empty_required_fields = 'Email, password and name are required fields'
    action_without_auth = 'You should be authorised'
    order_empty_error = 'Ingredient ids must be provided'
    server_error = 'Internal Server Error'


class TestData:
    without_name = {"email": "test@yandex.ru", "password": "test123"}
    without_email = {"password": "test123", "name": "johndoe"}
    without_password = {"email": "test@yandex.ru", "name": "johndoe"}


class Ingredients:
    valid_ingredients = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa6d",
            "61c0c5a71d1f82001bdaaa73"
        ]
    }
    invalid_ingredients = {
        "ingredients": [
            "nanana",
            "pupupu"
        ]
    }
