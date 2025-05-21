import pytest
import allure
from helpers import *
from urls import ErrorMessage, Urls
from user_data import generate_users


class TestCreateUser:
    @allure.title('Проверка создания нового пользователя')
    def test_create_user(self):
        payload = generate_users()
        response = requests.post(Urls.CREATE_USER_URL, data=payload)
        delete_user(response)
        assert response.status_code == 200 and 'accessToken' in response.text


    @allure.title('Проверка создания уже существующего пользователя')
    def test_create_user_twice(self):
        created_data = generate_users()
        response_first = requests.post(Urls.CREATE_USER_URL, data=created_data)
        response_second = requests.post(Urls.CREATE_USER_URL, data=created_data)
        assert response_second.status_code == 403 and response_second.json()['message'] == ErrorMessage.TEXT_CREATE_403_DOUBLE

    @allure.title('Создание пользователя без одного параметра')
    @pytest.mark.parametrize('data', ['email', 'name', 'password'])
    def test_create_user_without_one_data(self, data):
        payload = generate_users()
        del payload[data]
        response = create_user(payload)
        assert response.status_code == 403 and response.json()['message'] == ErrorMessage.TEXT_CREATE_403_WRONG