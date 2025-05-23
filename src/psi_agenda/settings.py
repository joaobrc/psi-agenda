from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='UTF-8'
    )

    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITOMO: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_MEMORIA: str
