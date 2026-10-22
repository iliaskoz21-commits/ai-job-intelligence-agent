from pydantic import BaseModel, Field


class Candidate(BaseModel):
    """Structured profile of a person looking for a job."""

    name: str = Field(min_length=1, description="Candidate's name")
    professional_title: str = Field(
        min_length=1,
        description="Candidate's current or target professional title",
    )
    skills: list[str] = Field(
        min_length=1,
        description="Candidate's professional skills",
    )
    years_experience: float = Field(
        ge=0,
        description="Years of professional experience",
    )
    education: list[str] = Field(default_factory=list)
    preferred_locations: list[str] = Field(default_factory=list)
    summary: str | None = None
