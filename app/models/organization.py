from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Organization(Base):
    """
    Represents a company using the AI Sales Call Intelligence System.
    """

    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False, unique=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    # One organization has many teams
    teams = relationship(
        "Team",
        back_populates="organization",
        cascade="all, delete-orphan"
    )