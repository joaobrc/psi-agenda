from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import Settings

config = Settings()

DATABASE_URI = config.DATABASE_URL

engine = create_engine(DATABASE_URI, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(bind=engine, autoflush=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
