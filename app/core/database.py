"""
Centralized database engine for Atlas.
All database interactions should use this shared engine.
"""

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from app.models.note import Base
from app.core.config import DATABASE_URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

def get_db():
    db = SessionLocal()

    try: 
        yield db
    finally:
        db.close()

def check_database_connection() -> bool:
    """
    Returns True if PostgreSQL is reachable.
    Returns False otherwise.
    """

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return True

    except SQLAlchemyError:
        return False
    
def create_tables():
    Base.metadata.create_all(bind=engine)