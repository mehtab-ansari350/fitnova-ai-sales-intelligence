from fastapi import FastAPI

app = FastAPI(
    title="FitNova AI Sales Call Intelligence System",
    description="AI-powered platform for analyzing sales calls.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to FitNova AI Sales Call Intelligence System"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }