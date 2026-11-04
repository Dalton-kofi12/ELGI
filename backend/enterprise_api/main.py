from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="ELGI Enterprise API",
    description="Backend services for the ELGI Educational Ecosystem",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to ELGI Enterprise API",
        "status": "running",
        "version": "0.1.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ELGI Enterprise API",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
