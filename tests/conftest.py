from pytest import fixture
from requests import Session
from config import Url, Secrets
from endpoints.token import Token
from endpoints.employees import Employees


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="api",
        help="Select environment"
    )

@fixture(scope="session")
def init_session():
    return Session()

@fixture(scope="session")
def init_config(request):
    env_name = request.config.getoption("--env")
    config = Url(env_name)
    return config

@fixture(scope="session")
def init_token(init_session, init_config):
    return Token(init_session, init_config.BASE_URL)

@fixture
def init_employee(init_session, init_config, init_token):
    token = init_token.generate_token({
        "username": Secrets.USER_NAME,
        "password": Secrets.PASSWORD,
     })
    return Employees(init_session, init_config.BASE_URL, token)
