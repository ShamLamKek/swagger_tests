# conftest.py
import pytest
from config.api_client import ApiClient
from services.pet.pet_api import PetApi


@pytest.fixture #фикстура для создания коннекта
def api_client():
    conn = ApiClient()
    return conn

@pytest.fixture
def pet_api(api_client):
    pet_api = PetApi(api_client)
    return pet_api