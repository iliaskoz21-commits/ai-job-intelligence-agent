from pydantic import BaseModel, Field


class MatchResult(BaseModel):
    candidate_name: str
    job_title: str
    matched_required_skills: list[str]
    missing_required_skills: list[str]
    matched_preferred_skills: list[str]
    required_skill_match_percentage: float = Field(ge=0, le=100)
