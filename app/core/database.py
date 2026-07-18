"""
Centralized database engine for Atlas.
All database interactions should use this shared engine.
"""

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

from app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL)


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