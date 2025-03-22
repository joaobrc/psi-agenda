from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITOMO: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_MEMORIA: str
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf=8'
    )
