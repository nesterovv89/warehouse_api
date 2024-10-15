import os
from pydantic import BaseSettings
from dotenv import load_dotenv


load_dotenv()

class Settings(BaseSettings):
    app_title: str = 'Set a title for app in your env-file'
    postgres_user: str = os.getenv("POSTGRES_USER")
    postgres_password: str = os.getenv("POSTGRES_PASSWORD")
    postgres_server: str = os.getenv("POSTGRES_SERVER","localhost")
    postgres_port: str = os.getenv("POSTGRES_PORT",5432)
    postgres_db: str = os.getenv("POSTGRES_DB","test_db")
    DATABASE_URL = f"postgresql+asyncpg://{postgres_user}:{postgres_password}@{postgres_server}:{postgres_port}/{postgres_db}"

    class Config:
        env_file = '.env'


settings = Settings()
#print(settings.app_title)
#print(settings.database_url)