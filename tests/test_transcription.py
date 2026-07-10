from app.ai.transcription import transcribe_audio

from pathlib import Path

audio_path = Path("sample_audio/sample.mp3")

result = transcribe_audio(str(audio_path))

print("=" * 60)
print("Language :", result["language"])
print("=" * 60)
print(result["transcript"])
print("=" * 60)