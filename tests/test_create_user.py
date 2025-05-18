import pytest
import allure
from helpers import *
from urls import ErrorMessage, Urls
from user_data import generate_users


class TestCreateUser:
    @allure.title('Проверка создания нового пользователя')
    def test_create_user(self, create_and_delete_user):
        created_data = create_and_delete_user
        assert created_data.status_code == 200 and 'accessToken' in created_data.text


    @allure.title('Проверка создания уже существующего пользователя')
    def test_create_user_twice(self):
        created_data = generate_users()
        response_first = requests.post(Urls.CREATE_USER_URL, data=created_data)
        response_second = requests.post(Urls.CREATE_USER_URL, data=created_data)
        assert response_second.status_code == 403 and response_second.json()['message'] == ErrorMessage.TEXT_CREATE_403_DOUBLE

    @allure.title('Создание пользователя без email')
    def test_create_user_without_email(self):
        payload = generate_users()
        del payload['email']
        response = create_user(payload)
        assert response.status_code == 403 and response.json()['message'] == ErrorMessage.TEXT_CREATE_403_WRONG

    @allure.title('Создание пользователя без name')
    def test_create_user_without_name(self):
        payload = generate_users()
        del payload['name']
        response = create_user(payload)
        assert response.status_code == 403 and response.json()['message'] == ErrorMessage.TEXT_CREATE_403_WRONG

    @allure.title('Создание пользователя без password')
    def test_create_user_without_password(self):
        payload = generate_users()
        del payload['password']
        response = create_user(payload)
        assert response.status_code == 403 and response.json()['message'] == ErrorMessage.TEXT_CREATE_403_WRONG