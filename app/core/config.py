from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "aqlite:///./test.db"

settings = Settings()