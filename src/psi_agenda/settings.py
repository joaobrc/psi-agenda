from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(toml_file='config.toml')
    database_uri: str
    debug: bool
