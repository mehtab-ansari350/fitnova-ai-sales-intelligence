# FitNova AI Sales Intelligence - Design Document

## Overview

FitNova AI Sales Intelligence is an AI-powered Sales Quality Monitoring System that automates the evaluation of customer sales calls. The system accepts an audio recording, converts speech into text using Faster-Whisper, analyzes the conversation with Google Gemini, detects sales quality issues, generates recommendations, stores the results in a relational database, and provides a mechanism for human reviewers to submit feedback on AI-generated evaluations.

The solution demonstrates a complete end-to-end AI workflow, integrating speech recognition, large language models, RESTful APIs, persistent storage, and a lightweight demonstration dashboard.

---

# System Architecture

The application follows a layered architecture that separates presentation, business logic, AI processing, and data persistence.

```
                    Streamlit Dashboard
                           │
                           │ REST API
                           ▼
                    FastAPI Application
                           │
            ┌──────────────┼──────────────┐
            │              │              │
            ▼              ▼              ▼
      Service Layer    AI Pipeline    CRUD Layer
            │              │              │
            │      ┌───────┴────────┐     │
            │      │                │     │
            ▼      ▼                ▼     ▼
      File Storage  Faster-Whisper  Google Gemini
                           │
                           ▼
                    SQLite Database
```

---

# System Components

## FastAPI Application

The FastAPI application serves as the entry point for all client requests.

Responsibilities include:

- Exposing REST APIs
- Request validation
- Response serialization
- Dependency injection
- Automatic Swagger documentation

Implemented endpoints:

- Upload Sales Call
- Retrieve AI Analysis
- Submit Human Feedback

---

## Service Layer

The service layer contains the application's business logic.

Responsibilities include:

- Saving uploaded audio files
- Managing file storage
- Coordinating AI workflow execution
- Invoking database operations

---

## AI Processing Pipeline

The AI pipeline performs automated sales call evaluation.

Pipeline stages:

1. Audio upload
2. Speech transcription using Faster-Whisper
3. Transcript storage
4. Sales conversation analysis using Google Gemini
5. Sales quality scoring
6. Issue detection
7. Recommendation generation
8. Analysis persistence

---

## Database Layer

The application uses SQLAlchemy ORM to interact with a SQLite database.

The database stores:

- Organizations
- Teams
- Advisors
- Calls
- Transcript segments
- AI analysis
- Detected issues
- Human feedback

---

# Artificial Intelligence Components

## Speech Recognition

Model:

**Faster-Whisper (Base)**

Purpose:

Convert customer call recordings into text.

Reasons for selection:

- Fast inference
- Good transcription accuracy
- CPU-compatible
- Open-source
- Lightweight deployment

---

## Large Language Model

Model:

**Google Gemini**

Purpose:

Analyze customer conversations and generate structured sales quality evaluations.

Responsibilities:

- Sales quality scoring
- Conversation summarization
- Issue detection
- Recommendation generation
- Structured JSON output

Reasons for selection:

- Strong reasoning capability
- Reliable structured responses
- Easy API integration
- High-quality natural language understanding

---

# Data Flow

```
Customer Call Recording
            │
            ▼
      Upload Audio File
            │
            ▼
      Store Audio File
            │
            ▼
     Create Call Record
            │
            ▼
 Speech-to-Text Transcription
     (Faster-Whisper)
            │
            ▼
     Store Transcript
            │
            ▼
      Google Gemini
            │
            ▼
 Sales Quality Analysis
            │
      ┌─────┼──────────────┐
      │     │              │
      ▼     ▼              ▼
 Score Issues Recommendations
      │
      ▼
 Store Analysis Results
      │
      ▼
 Human Feedback Submission
```

---

# Database Design

The system consists of the following relational entities.

## Organization

Represents an organization using the platform.

---

## Team

Represents a sales team within an organization.

---

## Advisor

Represents an individual sales advisor responsible for customer calls.

---

## Call

Stores uploaded sales call metadata.

Attributes include:

- Advisor
- Customer
- Audio file path
- Duration
- Language
- Processing status

---

## TranscriptSegment

Stores transcript segments generated from the speech recognition model.

Each segment contains:

- Speaker
- Start time
- End time
- Transcript text

---

## Analysis

Stores AI-generated analysis results.

Includes:

- Overall score
- Summary
- Recommendations

---

## Issue

Stores detected sales quality issues.

Each issue includes:

- Category
- Severity
- Evidence
- Timestamp

---

## Feedback

Stores human reviewer feedback.

Includes:

- Reviewer
- Decision
- Comment
- Timestamp

---

# REST API Design

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/calls/upload` | Upload a sales call and trigger AI processing |
| GET | `/calls/{call_id}/analysis` | Retrieve AI-generated analysis |
| POST | `/calls/{call_id}/feedback` | Submit reviewer feedback |

---

# Design Decisions

## FastAPI

Selected because it provides:

- High performance
- Automatic OpenAPI documentation
- Built-in validation using Pydantic
- Clean dependency injection
- Excellent developer productivity

---

## SQLAlchemy

Selected because it provides:

- ORM abstraction
- Database independence
- Relationship management
- Clean model definitions
- Easy maintenance

---

## SQLite

Selected because:

- No external database server is required
- Simple project setup
- Lightweight deployment
- Appropriate for prototype and assignment development

---

## Faster-Whisper

Selected because:

- Efficient CPU inference
- High transcription accuracy
- Low memory requirements
- Open-source implementation

---

## Google Gemini

Selected because it provides:

- Advanced reasoning capability
- High-quality conversational analysis
- Reliable structured JSON responses
- Excellent prompt-following performance

---

# Assumptions

The implementation assumes the following:

- Uploaded audio recordings are clear and understandable.
- Each recording contains one advisor and one customer.
- Google Gemini returns valid structured JSON.
- Advisor records already exist in the database.
- Internet connectivity is available during AI analysis.
- Audio files are supported by Faster-Whisper.

---

# Current Limitations

The current implementation intentionally excludes the following features:

- Speaker diarization
- Real-time streaming transcription
- Authentication
- Authorization
- Background task processing
- Distributed task queues
- Multi-language speech recognition
- Human feedback model retraining
- Batch call processing

These features are considered future enhancements rather than assignment requirements.

---

# Future Enhancements

Potential future improvements include:

- Speaker diarization
- Real-time call analysis
- Sentiment analysis
- Emotion detection
- Advisor performance dashboard
- Team-level analytics
- JWT authentication
- Role-based access control
- PostgreSQL migration
- Docker deployment
- Celery background workers
- Human-in-the-loop learning
- Retrieval-Augmented Generation (RAG) for coaching recommendations
- Multi-language support

---

# Conclusion

FitNova AI Sales Intelligence demonstrates a complete AI-powered sales quality monitoring workflow built using modern Python technologies.

The system integrates speech recognition, large language models, RESTful APIs, relational database storage, and a lightweight dashboard into a modular architecture. The implementation provides an extensible foundation for future enhancements while successfully meeting the core functional requirements of automated sales call evaluation and human feedback collection.