from sqlalchemy.orm import Session

from app.ai.transcription import transcribe_audio
from app.database.crud import create_transcript_segment
from app.database.crud import (
    update_call_after_transcription,
    create_analysis,
    create_issue,
)
from app.ai.analyzer import analyze_sales_call
from app.database.crud import create_analysis


def process_call(
    db: Session,
    call_id: int,
    audio_path: str,
):
    """
    End-to-end AI processing pipeline.
    """

    print("Starting transcription...")

    result = transcribe_audio(audio_path)

    print("Saving transcript...")

    for segment in result["segments"]:
        create_transcript_segment(
            db=db,
            call_id=call_id,
            speaker="UNKNOWN",
            start_time=segment["start"],
            end_time=segment["end"],
            text=segment["text"],
        )

    update_call_after_transcription(
        db=db,
        call_id=call_id,
        language=result["language"],
        duration=result["duration"],
    )


    print("Transcription saved.")

    print("Analyzing sales call...")

    analysis_result = analyze_sales_call(
        result["transcript"]
    )

    print("Saving analysis...")

    analysis = create_analysis(
        db=db,
        call_id=call_id,
        analysis_result=analysis_result,
    )

    print("Saving issues...")

    for issue in analysis_result.get("issues", []):
        create_issue(
            db=db,
            analysis_id=analysis.id,
            issue=issue,
        )

    print("Analysis and issues saved.")

    return result