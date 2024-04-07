import allure
import requests
from conftest import create_and_delete_user
from data import *


class TestGetOrder:
    @allure.title('Получение заказа доступно авторизованному пользователю')
    def test_user_get_order(self, create_and_delete_user):
        token = {'Authorization': create_and_delete_user[3]}
        requests_create_order = requests.post(Urls.ORDERS_URL, headers=token, data=Ingredients.valid_ingredients)
        response_get_order = requests.get(Urls.ORDERS_URL, headers=token)
        assert response_get_order.status_code == 200 and response_get_order.json()['orders'][0]['number'] == requests_create_order.json()['order']['number']

    @allure.title('Получение заказа не доступно авторизованному пользователю')
    def test_user_get_order_without_auth_error(self, create_and_delete_user):
        response = requests.get(Urls.ORDERS_URL)
        assert response.status_code == 401 and response.json()['message'] == Response.action_without_auth
