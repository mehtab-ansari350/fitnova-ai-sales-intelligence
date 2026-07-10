import requests

BASE_URL = "http://127.0.0.1:8000"


def upload_call(advisor_id, customer_name, audio_file):
    """
    Upload an audio file to the backend.
    """

    files = {
        "audio_file": (
            audio_file.name,
            audio_file,
            audio_file.type,
        )
    }

    data = {
        "advisor_id": advisor_id,
        "customer_name": customer_name,
    }

    response = requests.post(
        f"{BASE_URL}/calls/upload",
        data=data,
        files=files,
    )

    return response


def get_analysis(call_id):
    """
    Get AI analysis for a call.
    """

    response = requests.get(
        f"{BASE_URL}/calls/{call_id}/analysis"
    )

    return response


def submit_feedback(
    call_id,
    reviewer,
    decision,
    comment,
):
    """
    Submit advisor feedback.
    """

    payload = {
        "reviewer": reviewer,
        "decision": decision,
        "comment": comment,
    }

    response = requests.post(
        f"{BASE_URL}/calls/{call_id}/feedback",
        json=payload,
    )

    return response