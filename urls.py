class Urls:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site'
    CREATE_ORDER_URL = f'{MAIN_URL}/api/orders'
    GET_INGREDIENT_URL = f'{MAIN_URL}/api/ingredients'
    CREATE_USER_URL = f'{MAIN_URL}/api/auth/register'
    AUTHORIZATION_URL = f'{MAIN_URL}/api/auth/login'
    REGISTRATION_URL = f'{MAIN_URL}/api/auth/register'
    DELETE_USER_URL = f'{MAIN_URL}/api/auth/user'
    GET_USER_DATA = f'{MAIN_URL}/api/auth/user'
    UPDATE_USER_DATA = f'{MAIN_URL}/api/auth/user'


class ErrorMessage:
    TEXT_LOGIN_401 = 'email or password are incorrect'
    TEXT_LOGIN_404 = "Учетная запись не найдена"
    TEXT_CREATE_403_DOUBLE = "User already exists"
    TEXT_CREATE_403_WRONG = "Email, password and name are required fields"
    TEXT_CREATE_400 = "Недостаточно данных для создания учетной записи"
    TEXT_UPDATE_401 = "You should be authorised"
    TEXT_ORDER_WITHOUT_INGREDIENTS = "Ingredient ids must be provided"
    TEXT_GET_ORDERS_NO_AUTH = "You should be authorised"
