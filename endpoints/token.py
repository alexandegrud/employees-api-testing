from base.base_api import BaseApi

class Token(BaseApi):

    _endpoint = '/generate-token'

    def __init__(self, session, endpoint):
        super().__init__(session, endpoint)

    def generate_token(self, body):
        response = self.post(self._endpoint, json=body, headers=self.headers)
        return response.json()['token']