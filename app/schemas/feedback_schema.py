from datetime import datetime

from pydantic import BaseModel


class FeedbackCreate(BaseModel):
    """
    Request schema for advisor feedback.
    """

    reviewer: str
    decision: str
    comment: str | None = None


class FeedbackResponse(BaseModel):
    """
    Response schema.
    """

    id: int
    analysis_id: int
    reviewer: str
    decision: str
    comment: str | None
    created_at: datetime

    class Config:
        from_attributes = True