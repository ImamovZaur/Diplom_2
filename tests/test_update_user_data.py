import pytest
import allure
from urls import ErrorMessage
from helpers import *
from user_data import generate_email, generate_name, generate_users


class TestUpdateUserData:
    @allure.title('Проверка изменения email авторизованного пользователя')
    def test_update_email_authorized_user(self):
        user_create = create_and_authorization()
        token = get_token_user(user_create)
        email_update = generate_email()
        update_user = requests.patch(Urls.UPDATE_USER_DATA, headers={'Authorization': token}, data={'email': email_update})
        delete_user(user_create)
        assert update_user.status_code == 200 and update_user.json()['success'] == True

    @allure.title('Проверка изменения name авторизованного пользователя')
    def test_update_name_authorized_user(self):
        user_create = create_and_authorization()
        token = get_token_user(user_create)
        name_update = generate_name()
        update_user = requests.patch(Urls.UPDATE_USER_DATA, headers={'Authorization': token}, data={'email': name_update})
        delete_user(user_create)
        assert update_user.status_code == 200 and update_user.json()['success'] == True

    @allure.title('Проверка изменения данных не авторизованного пользователя')
    def test_update_data_without_authorized(self):
        user = generate_users()
        create_user(user)
        email_update = generate_email()
        response = requests.patch(Urls.UPDATE_USER_DATA, data={'email': email_update})
        assert response.status_code == 401 and response.json()['message'] == ErrorMessage.TEXT_UPDATE_401
