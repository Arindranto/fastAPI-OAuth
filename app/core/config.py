# my_microservice/app/core/config.py
import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables or .env file.
    """
    # Secret key for signing JWT tokens.
    # IMPORTANT: In a production environment, this should be a strong, randomly generated key.
    SECRET_KEY: str = os.getenv("SECRET_KEY", "super-secret-key-that-no-one-should-guess")
    ALGORITHM: str = "HS256" # Algorithm used for JWT signing
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30 # Token expiration time in minutes
    DATABASE_URL: str = "sqlite:///./sql_app.db"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()   # Initialize the setting