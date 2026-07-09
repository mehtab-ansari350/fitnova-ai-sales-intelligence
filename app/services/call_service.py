import os
import shutil
import uuid

from fastapi import UploadFile

UPLOAD_DIRECTORY = "uploads/audio"


def save_audio_file(audio_file: UploadFile) -> str:
    """
    Save uploaded audio to disk.
    """

    os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

    extension = os.path.splitext(audio_file.filename)[1]

    filename = f"{uuid.uuid4()}{extension}"

    file_path = os.path.join(
        UPLOAD_DIRECTORY,
        filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(audio_file.file, buffer)

    return file_path