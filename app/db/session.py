from app.core.config import get_settings, Settings

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



engine = create_engine(get_settings().DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
