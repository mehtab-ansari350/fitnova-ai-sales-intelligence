from sqlalchemy.orm import Session

from app.models.call import Call
from app.models.transcript import TranscriptSegment
from datetime import datetime

from app.database.enums import CallStatus
from app.models.analysis import Analysis
from app.models.feedback import Feedback

def create_call(
    db: Session,
    call: Call
):
    """
    Save a call into database.
    """

    db.add(call)
    db.commit()
    db.refresh(call)

    return call



def create_transcript_segment(
    db,
    call_id: int,
    speaker: str,
    start_time: float,
    end_time: float,
    text: str,
):
    """
    Save one transcript segment.
    """

    segment = TranscriptSegment(
        call_id=call_id,
        speaker=speaker,
        start_time=start_time,
        end_time=end_time,
        text=text,
    )

    db.add(segment)
    db.commit()
    db.refresh(segment)

    return segment



def update_call_after_transcription(
    db,
    call_id: int,
    language: str,
    duration: float,
):
    """
    Update call metadata after transcription.
    """

    call = db.query(Call).filter(Call.id == call_id).first()

    if not call:
        return None

    call.language = language
    call.duration_seconds = duration
    call.processing_status = CallStatus.COMPLETED
    call.processed_at = datetime.utcnow()

    db.commit()
    db.refresh(call)

    return call




def update_call_after_transcription(
    db,
    call_id: int,
    language: str,
    duration: float,
):
    """
    Update call metadata after transcription.
    """

    call = db.query(Call).filter(Call.id == call_id).first()

    if not call:
        return None

    call.language = language
    call.duration_seconds = duration
    call.processing_status = CallStatus.COMPLETED
    call.processed_at = datetime.utcnow()

    db.commit()
    db.refresh(call)

    return call

def create_analysis(
    db: Session,
    call_id: int,
    analysis_result: dict,
):
    """
    Save AI analysis into the database.
    """

    analysis = Analysis(
        call_id=call_id,
        overall_score=analysis_result["overall_score"],
        summary=analysis_result["summary"],
        recommendation="\n".join(
            analysis_result["recommendations"]
        )
    )

    db.add(analysis)
    db.commit()
    db.refresh(analysis)

    return analysis

def create_issue(
    db: Session,
    analysis_id: int,
    issue: dict,
):
    """
    Save one AI-detected issue.
    """

    from app.models.issue import Issue

    new_issue = Issue(
        analysis_id=analysis_id,
        issue_type=issue["category"],
        severity=issue["severity"],
        evidence=issue["evidence"],
        start_time=issue.get("start_time"),
        end_time=issue.get("end_time"),
        suggestion=issue.get("suggestion"),
    )

    db.add(new_issue)
    db.commit()
    db.refresh(new_issue)

    return new_issue


def get_analysis_by_call_id(
    db: Session,
    call_id: int,
):
    """
    Retrieve analysis by call ID.
    """

    return (
        db.query(Analysis)
        .filter(Analysis.call_id == call_id)
        .first()
    )

def create_feedback(
    db: Session,
    analysis_id: int,
    reviewer: str,
    decision: str,
    comment: str | None = None,
):
    """
    Save advisor feedback.
    """

    feedback = Feedback(
        analysis_id=analysis_id,
        reviewer=reviewer,
        decision=decision,
        comment=comment,
    )

    db.add(feedback)
    db.commit()
    db.refresh(feedback)

    return feedback