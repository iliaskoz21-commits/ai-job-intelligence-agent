from fastapi import FastAPI

from app.models.match_request import MatchRequest
from app.services.matching import match_candidate_to_job

app = FastAPI(
    title="AI Job Intelligence Agent",
    description="An AI-powered assistant for job analysis and career matching.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "AI Job Intelligence Agent is running",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/match")
def match(request: MatchRequest):
    return match_candidate_to_job(
        candidate=request.candidate,
        job=request.job,
    )
