import pytest
import allure
from urls import ErrorMessage
from helpers import *
from user_data import Ingredient


class TestCreateOrder:
    @allure.title('Создание заказа авторизованным пользователем')
    def test_create_order_with_authorized(self):
        user_create = create_and_authorization()
        token = get_token_user(user_create)
        response = requests.post(Urls.CREATE_ORDER_URL, headers={'Authorization': token} ,data=Ingredient.correct_ingredients_data)
        delete_user(user_create)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Создание заказа без авторизации пользователя')
    def test_create_order_without_authorized(self):
        response = requests.post(Urls.CREATE_ORDER_URL, data=Ingredient.correct_ingredients_data)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Создание заказа с неправильным хэшем ингредиентов')
    def test_create_order_incorrect_hash_ingredient(self):
        response = requests.post(Urls.CREATE_ORDER_URL, data=Ingredient.incorrect_ingredients_data)
        assert response.status_code == 500 and ErrorMessage.TEXT_ORDER_500 in response.text

    @allure.title('Создание заказа с ингредиентами')
    def test_create_order_with_ingredient(self):
        response = requests.post(Urls.CREATE_ORDER_URL, data=Ingredient.correct_ingredients_data)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredient(self):
        response = requests.post(Urls.CREATE_ORDER_URL, data=Ingredient.without_ingredient_data)
        assert response.status_code == 400 and response.json()['message'] == ErrorMessage.TEXT_ORDER_WITHOUT_INGREDIENTS