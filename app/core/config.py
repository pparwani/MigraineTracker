from typing import List

from pydantic import HttpUrl, field_validator, validator
from pydantic_settings import BaseSettings  # Assuming you've updated this

class Settings(BaseSettings):
    app_name: str
    admin_email: str
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    mongo_connection_string: str
    mongo_db: str
    backend_cors_origins: str='*'

    class Config:
        env_file = '.env'

settings = Settings()
print("Current settings:", settings.dict())  # This will show you what's actually being loaded