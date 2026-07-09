from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class CallResponse(BaseModel):
    """
    Response schema returned after creating or fetching a call.
    """

    id: int
    advisor_id: int
    call_uuid: str
    customer_name: str
    audio_file_path: str
    duration_seconds: Optional[float]
    language: Optional[str]
    processing_status: str
    uploaded_at: datetime
    processed_at: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)