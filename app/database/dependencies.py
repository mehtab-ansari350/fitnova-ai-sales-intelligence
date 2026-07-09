from sqlalchemy.orm import Session

from app.database.connection import SessionLocal


def get_db():
    """
    Database session dependency.
    """
    db: Session = SessionLocal()

    try:
        yield db
    finally:
        db.close()