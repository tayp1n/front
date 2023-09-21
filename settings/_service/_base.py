from abc import ABCMeta
from typing import Tuple


ENVIRONMENT: str = "Test"

SERVER_HOST: str = "0.0.0.0"
SERVER_PORT: int = 9090

WORKERS_COUNTS: int = 5

RELOAD: bool = False


class BaseSettings(metaclass=ABCMeta):
    pass


APP_NAME: str = "service"

CORE_API_HOST: str = "http://127.0.0.1:8081"

VERSION: str = ".version.json"

CORS_ORIGINS: Tuple[str, ...] = (
    "*",
)
