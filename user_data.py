from faker import Faker


class Ingredient:
    correct_ingredients_data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}

    incorrect_ingredients_data = {
        "ingredients": ["60d3b41abdacab0026a733c6g", "609646e4dc916e00276b2870g"]}

    without_ingredient_data = {
        "ingredients": []
    }


def generate_user_static_data():
    payload = {
        'email': 'practicum@ya.ru',
        'password': '1234567',
        'name': 'Naruto'
    }
    return payload

def generate_email():
    fake = Faker()
    email = fake.email()
    return email


def generate_password():
    fake = Faker()
    password = fake.password()
    return password


def generate_name():
    fake = Faker()
    name = fake.name()
    return name


def generate_users():
    payload = {
        "email": generate_email(),
        "password": generate_password(),
        "name": generate_name()
    }
    return payload
