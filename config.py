from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    NVIDIA_API_KEY: str


settings = Settings()
