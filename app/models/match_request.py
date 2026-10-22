from pydantic import BaseModel

from app.models.candidate import Candidate
from app.models.job import Job


class MatchRequest(BaseModel):
    candidate: Candidate
    job: Job
