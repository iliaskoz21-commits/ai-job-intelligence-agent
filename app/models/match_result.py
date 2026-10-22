
from pydantic import BaseModel, Field


class MatchResult(BaseModel):
    candidate_name: str
    job_title: str
    matched_required_skills: list[str]
    missing_required_skills: list[str]
    matched_preferred_skills: list[str]
    required_skill_match_percentage: float = Field(ge=0, le=100)

    candidate_years_experience: float = Field(ge=0)
    required_years_experience: float = Field(ge=0)
    meets_experience_requirement: bool

    match_summary: str
