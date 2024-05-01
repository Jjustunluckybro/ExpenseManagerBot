import os
from typing import Final, Any

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class EnvDependNotFound(Exception):
    pass


def get_env_var(var_name: str) -> Any:
    """
    :raise EnvDependNotFound if value in None
    :param var_name: Env var name
    :return: Var value by name
    """
    value: Any = os.getenv(var_name)
    if value is None:
        raise EnvDependNotFound(var_name)
    else:
        return value


class Config:
    DB_HOST: Final[str] = get_env_var("DB_HOST")
    DB_PORT: Final[int] = get_env_var("DB_PORT")
    DB_USER: Final[str] = get_env_var("DB_USER")
    DB_PASSWORD: Final[str] = get_env_var("DB_PASSWORD")
    DB_NAME: Final[str] = get_env_var("DB_NAME")

    @property
    def db_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


CONFIG = Config()
