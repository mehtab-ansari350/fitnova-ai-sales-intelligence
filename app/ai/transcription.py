from faster_whisper import WhisperModel

# Load model only once
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)


def transcribe_audio(audio_path: str):
    """
    Transcribe an audio file using Faster Whisper.
    Returns:
        - language
        - duration
        - full transcript
        - transcript segments with timestamps
    """

    segments, info = model.transcribe(audio_path)

    transcript_segments = []
    full_transcript = ""

    for segment in segments:
        transcript_segments.append(
            {
                "start": round(segment.start, 2),
                "end": round(segment.end, 2),
                "text": segment.text.strip(),
            }
        )

        full_transcript += segment.text + " "

    return {
        "language": info.language,
        "duration": info.duration,
        "transcript": full_transcript.strip(),
        "segments": transcript_segments,
    }