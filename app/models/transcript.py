from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database.connection import Base


class TranscriptSegment(Base):
    """
    Represents one speaker segment from a sales call transcript.
    """

    __tablename__ = "transcript_segments"

    id = Column(Integer, primary_key=True, index=True)

    call_id = Column(
        Integer,
        ForeignKey("calls.id"),
        nullable=False
    )

    speaker = Column(
        String(20),
        nullable=False
    )

    start_time = Column(
        Float,
        nullable=False
    )

    end_time = Column(
        Float,
        nullable=False
    )

    text = Column(
        Text,
        nullable=False
    )

    call = relationship(
        "Call",
        back_populates="transcript_segments"
    )