#pet_api
from services.base_api import BaseApi

class PetApi(BaseApi):
    def __init__(self, api_client):
        super().__init__(api_client, '/pet')