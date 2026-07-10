from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Issue(Base):
    """
    Represents an issue detected during AI analysis.
    """

    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, index=True)

    analysis_id = Column(
        Integer,
        ForeignKey("analyses.id"),
        nullable=False
    )

    issue_type = Column(
        String(100),
        nullable=False
    )

    severity = Column(
        String(20),
        nullable=False
    )

    evidence = Column(
        Text,
        nullable=False
    )

    start_time = Column(
        Float,
        nullable=True
    )

    end_time = Column(
        Float,
        nullable=True
    )

    suggestion = Column(
        Text,
        nullable=True
    )

    analysis = relationship(
        "Analysis",
        back_populates="issues"
    )