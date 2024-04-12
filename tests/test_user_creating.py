import pytest
import allure
import requests
from conftest import create_and_delete_user
from data import *
from helpers import create_user_data


class TestCreateUser:
    @allure.title('Успешная регистрация нового пользователя')
    def test_user_unique_creating(self, create_and_delete_user):
        payload = create_user_data()
        response = requests.post(Urls.REGISTER_URL, data=payload)
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title('Ошибка при создании пользователя')
    @allure.description('Попытка зарегистрировать уже существующего пользователя')
    def test_user_existing_creating(self, create_and_delete_user):
        response = requests.post(Urls.REGISTER_URL, data=create_and_delete_user[1])
        assert response.status_code == 403 and response.json()['message'] == Response.exist_user_error

    @allure.title('Ошибка регистрации без ввода обязательных полей')
    @allure.description('Если нет одного из полей, вернётся код ответа 403')
    @pytest.mark.parametrize('required_fields',
                             (TestData.without_name, TestData.without_email, TestData.without_password))
    def test_user_empty_creating(self, required_fields):
        response = requests.post(Urls.REGISTER_URL, data=required_fields)
        assert response.status_code == 403 and response.json()['message'] == Response.empty_required_fields
