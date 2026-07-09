from enum import Enum


class CallStatus(str, Enum):
    """
    Processing stages of an uploaded sales call.
    """

    UPLOADED = "uploaded"
    TRANSCRIBING = "transcribing"
    DIARIZING = "diarizing"
    ANALYZING = "analyzing"
    COMPLETED = "completed"
    FAILED = "failed"