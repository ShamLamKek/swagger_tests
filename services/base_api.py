#base_api

class BaseApi:
    def __init__(self, api_client, endpoint):
        self.api_client = api_client
        self.endpoint = endpoint

    def post(self, body):
        url = self.api_client.base_url+self.endpoint
        response = self.api_client.session.post(url, json=body)
        return response

    def put(self):
        pass

    def get(self):
        pass

    def delete(self):
        pass


