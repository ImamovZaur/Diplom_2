import pytest
import requests
from helpers import get_token_user
from user_data import generate_users
from urls import *

@pytest.fixture()
def create_and_delete_user():
    payload = generate_users()
    response = requests.post(Urls.CREATE_USER_URL, data=payload)
    yield response
    token = get_token_user(response)
    requests.delete(Urls.DELETE_USER_URL, headers={'Authorization': token})