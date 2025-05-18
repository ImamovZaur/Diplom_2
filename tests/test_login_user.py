import pytest
import allure
from urls import ErrorMessage
from helpers import *
from user_data import generate_users, generate_password


class TestLoginUser:
    @allure.title('Проверка успешной авторизации созданного пользователя')
    def test_authorization_user(self):
        response = create_and_authorization()
        delete_user(response)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Проверка авторизации пользователя с неверным паролем')
    def test_authorization_user_wrong_password(self):
        payload = generate_users()
        create_user(payload)
        del payload['name']
        payload['password'] = generate_password()
        response = requests.post(Urls.AUTHORIZATION_URL, data=payload)
        assert response.status_code == 401 and response.json()['message'] == ErrorMessage.TEXT_LOGIN_401