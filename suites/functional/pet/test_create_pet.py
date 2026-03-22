#test_create_pet
import allure


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
        assert response_data["name"] == "doggie"
        assert response_data["id"] is not None