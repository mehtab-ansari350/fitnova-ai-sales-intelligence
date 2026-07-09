from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Feedback(Base):
    """
    Stores human feedback on AI analysis.
    """

    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)

    analysis_id = Column(
        Integer,
        ForeignKey("analyses.id"),
        nullable=False
    )

    reviewer = Column(
        String(100),
        nullable=False
    )

    decision = Column(
        String(20),
        nullable=False
    )

    comment = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    analysis = relationship(
        "Analysis",
        back_populates="feedback"
    )