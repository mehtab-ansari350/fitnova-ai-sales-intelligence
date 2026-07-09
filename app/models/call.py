from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from app.database.connection import Base
from app.database.enums import CallStatus

class Call(Base):
    """
    Represents a sales call uploaded by an advisor.
    """

    __tablename__ = "calls"

    id = Column(Integer, primary_key=True, index=True)

    advisor_id = Column(
        Integer,
        ForeignKey("advisors.id"),
        nullable=False
    )

    call_uuid = Column(
        String(50),
        unique=True,
        nullable=False,
        index=True
    )

    customer_name = Column(
        String(100),
        nullable=False
    )

    audio_file_path = Column(
        String(255),
        nullable=False
    )

    duration_seconds = Column(
        Float,
        nullable=True
    )

    language = Column(
        String(30),
        nullable=True
    )

    processing_status = Column(
        Enum(CallStatus),
        default=CallStatus.UPLOADED,
        nullable=False
    )

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    processed_at = Column(
        DateTime,
        nullable=True
    )

    advisor = relationship(
        "Advisor",
        back_populates="calls"
    )

    transcript_segments = relationship(
    "TranscriptSegment",
    back_populates="call",
    cascade="all, delete-orphan"
    )

    analysis = relationship(
    "Analysis",
    back_populates="call",
    uselist=False,
    cascade="all, delete-orphan"
    )