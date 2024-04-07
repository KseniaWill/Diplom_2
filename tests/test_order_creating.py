import allure
import requests
from conftest import create_and_delete_user
from data import *


class TestOrderCreating:
    @allure.title('Успешное создание заказа авторизованным пользователем')  # декораторы
    def test_order_creating(self, create_and_delete_user):
        token = {'Authorization': create_and_delete_user[3]}
        response = requests.post(Urls.ORDERS_URL, headers=token, data=Ingredients.valid_ingredients)
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title('Создание заказа пользователем без авторизации')
    def test_order_creating_without_auth(self, create_and_delete_user):
        response = requests.post(Urls.ORDERS_URL, data=Ingredients.valid_ingredients)
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title('Ошибка при создании заказа без ингредиентов')
    @allure.description('Если не передать ни один ингредиент, вернётся код ответа 400 Bad Request')
    def test_order_creating_without_data(self, create_and_delete_user):
        response = requests.post(Urls.ORDERS_URL)
        assert response.status_code == 400 and response.json()['message'] == Response.order_empty_error

    @allure.title('Ошибка при создании заказа c несуществующими ингредиентами')
    @allure.description('Если в теле запроса передан невалидный хеш ингредиента, то вернется ошибка сервера')
    def test_create_order_incorrect_hash_fail(self, create_and_delete_user):
        response = requests.post(Urls.ORDERS_URL, data=Ingredients.invalid_ingredients)
        assert response.status_code == 500 and Response.server_error in response.text
