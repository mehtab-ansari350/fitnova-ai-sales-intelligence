import uuid

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.database.crud import create_call
from app.database.enums import CallStatus
from app.models.call import Call
from app.schemas.call_schema import CallResponse
from app.services.call_service import save_audio_file
from app.ai.pipeline import process_call
from app.database.crud import get_analysis_by_call_id
from app.schemas.analysis_schema import AnalysisResponse
from app.schemas.feedback_schema import (
    FeedbackCreate,
    FeedbackResponse,
)
from app.database.crud import (
    create_feedback,
    get_analysis_by_call_id,
)


router = APIRouter(
    prefix="/calls",
    tags=["Calls"]
)

@router.post(
    "/upload",
    response_model=CallResponse,
    status_code=201
)
def upload_call(
    advisor_id: int = Form(...),
    customer_name: str = Form(...),
    audio_file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    Upload a sales call.
    """

    if not audio_file.filename:
        raise HTTPException(
            status_code=400,
            detail="Audio file is required."
        )

    file_path = save_audio_file(audio_file)

    call = Call(
        call_uuid=str(uuid.uuid4()),
        advisor_id=advisor_id,
        customer_name=customer_name,
        audio_file_path=file_path,
        processing_status=CallStatus.UPLOADED,
    )

    call = create_call(db, call)
    try:
        # Start AI processing
        process_call(
            db=db,
            call_id=call.id,
            audio_path=file_path,
        )
    except Exception as e:
        print(f"Pipeline error: {e}")

    return call

@router.get(
    "/{call_id}/analysis",
    response_model=AnalysisResponse
)
def get_call_analysis(
    call_id: int,
    db: Session = Depends(get_db)
):
    """
    Get AI analysis for a sales call.
    """

    analysis = get_analysis_by_call_id(db, call_id)

    if analysis is None:
        raise HTTPException(
            status_code=404,
            detail="Analysis not found."
        )

    return analysis

@router.post(
    "/{call_id}/feedback",
    response_model=FeedbackResponse,
    status_code=201,
)
def submit_feedback(
    call_id: int,
    feedback: FeedbackCreate,
    db: Session = Depends(get_db),
):
    """
    Submit advisor feedback for a call analysis.
    """

    analysis = get_analysis_by_call_id(
        db=db,
        call_id=call_id,
    )

    if not analysis:
        raise HTTPException(
            status_code=404,
            detail="Analysis not found."
        )

    return create_feedback(
        db=db,
        analysis_id=analysis.id,
        reviewer=feedback.reviewer,
        decision=feedback.decision,
        comment=feedback.comment,
    )