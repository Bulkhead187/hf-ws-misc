from pydantic_settings import BaseSettings
from pydantic import Field
import os
from dotenv import load_dotenv
# hi ivan cyberbyte here
load_dotenv()

class Settings(BaseSettings):
    NVIDIA_API_KEY: str = Field(default=..., env="NVIDIA_API_KEY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
