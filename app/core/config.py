import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
  APP_NAME: str = os.getenv("APP_NAME", "HabitApp")
  APP_VERSION: str = os.getenv("APP_VERSION", "0.1.0")

  DB_HOST: str = os.getenv("DB_HOST", "localhost")
  DB_PORT: int = int(os.getenv("DB_PORT", 3306))
  DB_USER: str = os.getenv("DB_USER", "root")
  DB_PASSWORD: str = os.getenv("DB_PASSWORD", "121314")
  DB_NAME: str = os.getenv("DB_NAME", "habit_db")

  SQLALCHEMY_DATABASE_URI: str = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
    )
  
  JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "")
  JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
  JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", 30))

settings = Settings()
