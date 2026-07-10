from datetime import datetime

from pydantic import BaseModel, ConfigDict


class AnalysisResponse(BaseModel):
    id: int
    call_id: int
    overall_score: int
    summary: str
    recommendation: str | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)