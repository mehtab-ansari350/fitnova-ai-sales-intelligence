from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)

from sqlalchemy.orm import relationship

from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

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

    name = Column(String(100), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship back to organization
    organization = relationship(
        "Organization",
        back_populates="teams"
    )

    advisors = relationship(
    "Advisor",
    back_populates="team",
    cascade="all, delete-orphan"
    )


class Advisor(Base):
    """
    Represents a sales advisor.
    """

    __tablename__ = "advisors"

    id = Column(Integer, primary_key=True, index=True)

    team_id = Column(
        Integer,
        ForeignKey("teams.id"),
        nullable=False
    )

    employee_id = Column(
        String(20),
        unique=True,
        nullable=False
    )

    full_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(150),
        unique=True,
        nullable=False
    )

    phone = Column(
        String(20),
        nullable=True
    )

    status = Column(
        String(20),
        default="Active"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    team = relationship(
        "Team",
        back_populates="advisors"
    )

    calls = relationship(
        "Call",
        back_populates="advisor",
        cascade="all, delete-orphan"
    )


    