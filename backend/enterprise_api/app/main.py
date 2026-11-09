from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="ELGI Enterprise API",
    description="Enterprise services for ELGI Ghana",
    version="0.2.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to ELGI Enterprise API",
        "status": "running",
        "version": app.version,
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "ELGI Enterprise API",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
