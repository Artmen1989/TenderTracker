from fastapi import FastAPI
from app.routers import tenders

app = FastAPI(title="Tender Tracker", version="1.0.0")

app.include_router(tenders.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}