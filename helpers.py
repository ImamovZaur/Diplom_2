import requests
from urls import Urls
from user_data import *


def create_user(user_data):
    response = requests.post(Urls.CREATE_USER_URL, data=user_data)
    return response


def get_token_user(data):
    token = data.json().get('accessToken')
    return token


def delete_user(data):
    token = get_token_user(data)
    response = requests.delete(Urls.DELETE_USER_URL, headers={'Authorization': token})


def create_and_authorization():
    data_user = generate_users()
    create_user(data_user)
    del data_user['name']
    response = requests.post(Urls.AUTHORIZATION_URL, data=data_user)
    return response
