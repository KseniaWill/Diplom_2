import allure
import requests
from conftest import create_and_delete_user
from data import Urls, Response
from helpers import create_user_login


class TestLoginUser:
    @allure.title('Авторизация выполнена')
    @allure.description('При вводе валидного логина и пароля, авторизация выполняется')
    def test_user_correct_auth(self, create_and_delete_user):
        response = requests.post(Urls.LOGIN_URL, data=create_and_delete_user[2])
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title('Ошибка авторизации')
    @allure.description('Попытка авторизации с невалидным логином и паролем')
    def test_user_incorrect_auth(self, create_and_delete_user):
        payload = create_user_login()
        response = requests.post(Urls.LOGIN_URL, data=payload)
        assert response.status_code == 401 and response.json()['message'] == Response.user_auth_error
