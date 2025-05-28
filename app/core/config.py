from pydantic_settings import BaseSettings
from typing import Optional, List
import secrets
from functools import lru_cache

class Settings(BaseSettings):
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "ParkPerks AI"
    
    # Security
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    
    # Database
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "parkperks"
    SQLALCHEMY_DATABASE_URI: Optional[str] = None
    
    # AI Model Settings
    MODEL_PATH: str = "models/parkperks_model.pt"
    EMBEDDING_DIM: int = 128
    BATCH_SIZE: int = 32
    
    # Parking Settings
    MAX_SPONSORED_HOURS: int = 24
    MIN_SPONSORED_HOURS: int = 1
    
    class Config:
        case_sensitive = True
        env_file = ".env"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.SQLALCHEMY_DATABASE_URI:
            self.SQLALCHEMY_DATABASE_URI = (
                f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"
            )

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings() 