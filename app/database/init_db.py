from app.database.connection import Base, engine

# Import all models so SQLAlchemy knows about them
from app.models import (
    Organization,
    Team,
    Advisor,
    Call,
    TranscriptSegment,
    Analysis,
    Issue,
    Feedback,
)


def init_db():
    """
    Create all database tables.
    """
    Base.metadata.create_all(bind=engine)