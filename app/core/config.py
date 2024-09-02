from typing import Any, List

from pydantic import HttpUrl, field_validator, validator
from pydantic_settings import BaseSettings  # Assuming you've updated this
import json

class Settings(BaseSettings):
    app_name: str
    admin_email: str
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    mongo_connection_string: str
    mongo_db: str
    backend_cors_origins: List[str]=['*']
    
    @field_validator("backend_cors_origins",mode='after')
    def assemble_cors_origins(cls, v: Any) -> List[str]:
        if isinstance(v, str):
            return json.loads(v)
        elif isinstance(v, list):
            return v
        raise ValueError("Invalid value for backend_cors_origins")
    

    class Config:
        env_file = '.env'

settings = Settings()