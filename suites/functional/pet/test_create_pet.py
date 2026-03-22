#test_create_pet
import allure
from services.pet.pet_model import PetResponse


@allure.feature("Pet")  # группа функциональности
@allure.story("Create pet")  # конкретная история
@allure.title("Позитивный тест создания питомца")  # название теста
def test_create_pet_positive(pet_api):
    with allure.step("Подготовить тело запроса"):
        body = {
            "name": "doggie",
            "photoUrls": ["string"]
        }

    with allure.step("Отправить POST запрос"):
        response = pet_api.post(body)

    with allure.step("Проверить ответ"):
        assert response.status_code == 200
        response_data = response.json()
        pet = PetResponse(**response_data)  # валидация через Pydantic
        assert pet.name == "doggie"
        assert pet.id is not None


@allure.feature("Pet")  # группа функциональности
@allure.story("Create pet")  # конкретная история
@allure.title("Негативный тест создания питомца")  # название теста
def test_create_pet_negative(pet_api):
    with allure.step("Подготовить тело запроса"):
        body = {
            "name": 123,
            "photoUrls": 123
        }

    with allure.step("Отправить POST-запрос"):
        response = pet_api.post(body)

    with allure.step("Проверить ответ"):
        assert response.status_code == 405