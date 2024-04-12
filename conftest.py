import pytest
from helpers import *
from data import Urls
import requests


@pytest.fixture(scope="function")
def create_and_delete_user():
    payload = create_user_data()
    login_data = payload.copy()
    del login_data["name"]
    response = requests.post(Urls.REGISTER_URL, data=payload)
    token = response.json()["accessToken"]
    yield response, payload, login_data, token
    requests.delete(Urls.USER_URL, headers={'Authorization': f'{token}'})

    def test_user_login_success(self, create_and_delete_user):
        response = requests.post(Urls.LOGIN_URL, data=create_and_delete_user[2])
        assert response.status_code == 200 and response.json().get("success") is True