from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Team(Base):
    """
    Represents a sales team within an organization.
    """

    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id"),
        nullable=False
    )

    name = Column(
        String(100),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # Relationship back to Organization
    organization = relationship(
        "Organization",
        back_populates="teams"
    )

    # One Team has many Advisors
    advisors = relationship(
        "Advisor",
        back_populates="team",
        cascade="all, delete-orphan"
    )