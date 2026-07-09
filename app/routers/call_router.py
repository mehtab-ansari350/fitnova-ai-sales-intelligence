import uuid

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.database.crud import create_call
from app.models.call import Call
from app.schemas.call_schema import CallResponse
from app.services.call_service import save_audio_file

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
        advisor_id=advisor_id,
        call_uuid=str(uuid.uuid4()),
        customer_name=customer_name,
        audio_file_path=file_path,
    )

    return create_call(db, call)