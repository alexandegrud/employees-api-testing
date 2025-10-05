from dotenv import load_dotenv
from typing import Final
import os

load_dotenv()



class Url:
    def __init__(self, env_config: str):
        self.BASE_URL: Final[str] = os.getenv("BASE_URL").format(env_config).lower()


class Secrets:

    USER_NAME: Final[str] = os.getenv("USER_NAME")
    PASSWORD: Final[str] = os.getenv("PASSWORD")