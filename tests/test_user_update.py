import pytest
import allure
import requests
from conftest import create_and_delete_user
from data import Urls, Response
from helpers import generate_random_string


class TestChangeUserData:
    @allure.title('Успешное изменение почты авторизованного пользователя')
    def test_user_update_email_auth_success(self, create_and_delete_user):
        new_email = f'{generate_random_string(5)}@yandex.ru'
        required_field = {'email': new_email}
        token = {'Authorization': create_and_delete_user[3]}
        response = requests.patch(Urls.USER_URL, headers=token, data=required_field)
        assert response.status_code == 200 and response.json()['user']['email'] == new_email

    @allure.title('Успешное изменение пароля авторизованного пользователя')
    def test_user_update_password_auth_success(self, create_and_delete_user):
        new_password = generate_random_string(5)
        required_field = {'password': new_password}
        token = {'Authorization': create_and_delete_user[3]}
        response = requests.patch(Urls.USER_URL, headers=token, data=required_field)
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title('Успешное изменение имени авторизованного пользователя')
    def test_user_update_name_auth_success(self, create_and_delete_user):
        new_name = generate_random_string(5)
        required_field = {'name': new_name}
        token = {'Authorization': create_and_delete_user[3]}
        response = requests.patch(Urls.USER_URL, headers=token, data=required_field)
        assert response.status_code == 200 and response.json()['user']['name'] == new_name

    @allure.title('Ошибка при изменении данных неавторизованного пользователя')
    @pytest.mark.parametrize('required_fields', [{'email': f'{generate_random_string(5)}@yandex.ru'},
                                                 {'password': generate_random_string(5)},
                                                 {'name': generate_random_string(5)}])
    def test_user_update_without_auth_error(self, required_fields):
        response = requests.patch(Urls.USER_URL, data=required_fields)
        assert response.status_code == 401 and response.json()['message'] == Response.action_without_auth
