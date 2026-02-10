"""
Amaç:
“Hardcode yok, yarın prod’a çıkarsam ağlamayayım”
"""


from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "StyleMind API"
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/stylemind"

    class Config:
        env_file = ".env"

settings = Settings()
