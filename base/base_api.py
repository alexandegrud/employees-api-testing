from requests import Session
from helper.assertions import Assertions

class BaseApi:

    def __init__(self, session: Session, url: str) -> None:
        self.session = session
        self.url = url
        self.headers = {
            'Content-Type': 'application/json',
        }
        self.assertions = Assertions

    def get(self, endpoint, **kwargs):
        response = self.session.get(f"{self.url}{endpoint}", **kwargs)
        return response

    def post(self, endpoint, **kwargs):
        response = self.session.post(f"{self.url}{endpoint}", **kwargs)
        return response

    def put(self, endpoint, **kwargs):
        response = self.session.put(f"{self.url}{endpoint}", **kwargs)
        return response

    def patch(self, endpoint, **kwargs):
        response = self.session.patch(f"{self.url}{endpoint}", **kwargs)
        return response

    def delete(self, endpoint, **kwargs):
        response = self.session.delete(f"{self.url}{endpoint}", **kwargs)
        return response