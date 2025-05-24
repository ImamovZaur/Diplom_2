import pytest
import allure
from urls import ErrorMessage
from helpers import *
from user_data import Ingredient


class TestGetOrders:
    @allure.title('Получение списка заказов авторизованного пользователя')
    def test_get_order_authorized_user(self):
        user_create = create_and_authorization()
        token = get_token_user(user_create)
        requests.post(Urls.CREATE_ORDER_URL, headers={'Authorization': token}, data=Ingredient.correct_ingredients_data)
        response = requests.get(Urls.CREATE_ORDER_URL, headers={'Authorization': token})
        assert response.status_code == 200 and 'orders' in response.text

    @allure.title('Получение списка заказов без авторизации')
    def test_get_order_without_authorized_user(self):
        requests.post(Urls.CREATE_ORDER_URL, data=Ingredient.correct_ingredients_data)
        response = requests.get(Urls.CREATE_ORDER_URL)
        assert response.status_code == 401 and response.json()['message'] == ErrorMessage.TEXT_GET_ORDERS_NO_AUTH