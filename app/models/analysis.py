from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Analysis(Base):
    """
    Stores AI-generated analysis for a sales call.
    """

    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True, index=True)

    call_id = Column(
        Integer,
        ForeignKey("calls.id"),
        nullable=False,
        unique=True
    )

    overall_score = Column(
        Float,
        nullable=False
    )

    summary = Column(
        Text,
        nullable=False
    )

    recommendation = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    call = relationship(
        "Call",
        back_populates="analysis"
    )

    issues = relationship(
        "Issue",
        back_populates="analysis",
        cascade="all, delete-orphan"
    )

    feedback = relationship(
        "Feedback",
        back_populates="analysis",
        cascade="all, delete-orphan"
    )