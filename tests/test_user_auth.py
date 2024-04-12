import allure
import requests
from conftest import create_and_delete_user
from data import *
from helpers import *


class TestLoginUser:
    @allure.title('Успешная авторизация пользователя')
    def test_user_login_success(self, create_and_delete_user):
        response = requests.post(Urls.LOGIN_URL, data=create_and_delete_user[2])
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title('Ошибка при авторизации с неверным логином')
    def test_user_login_incorrect_login_data(create_and_delete_user):
        response = requests.post(Urls.LOGIN_URL,
                                 data={"username": "incorrect_username", "password": "correct_password"})
        assert response.status_code == 401 and response.json()['message'] == Response.user_auth_error

    @allure.title('Ошибка при авторизации с неверным паролем')
    def test_user_login_incorrect_password(create_and_delete_user):
        response = requests.post(Urls.LOGIN_URL,
                                 data={"username": "correct_username", "password": "incorrect_password"})
        assert response.status_code == 401 and response.json()['message'] == Response.user_auth_error