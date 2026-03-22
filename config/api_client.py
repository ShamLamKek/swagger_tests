import requests


BASE_URL = "https://petstore.swagger.io/v2"
# класс инициализирующий подключение к API
class ApiClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url # передал URL
        self.session = requests.Session() # создал объект сессии
