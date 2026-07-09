from fastapi import FastAPI

from app.database.init_db import init_db
from app.routers.call_router import router as call_router

app = FastAPI(
    title="FitNova AI Sales Intelligence",
    version="1.0.0"
)


@app.on_event("startup")
def startup():
    init_db()


app.include_router(call_router)


@app.get("/")
def root():
    return {
        "message": "FitNova AI Sales Intelligence API is running"
    }