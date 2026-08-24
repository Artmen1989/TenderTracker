import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/tender_db")

engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Функция для получения сессии БД (используется в роутерах)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()