from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = Field(default='postgresql+asyncpg://crossfit:crossfit@localhost/crossfit')


settings = Settings()
