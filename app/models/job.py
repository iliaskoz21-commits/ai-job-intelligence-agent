from pydantic import BaseModel, Field


class Job(BaseModel):
    """Structured description of a job opening."""

    title: str = Field(min_length=1)
    company: str = Field(min_length=1)
    required_skills: list[str] = Field(min_length=1)
    preferred_skills: list[str] = Field(default_factory=list)
    min_years_experience: float = Field(default=0, ge=0)
    location: str | None = None
    remote: bool = False
    description: str = Field(min_length=1)
