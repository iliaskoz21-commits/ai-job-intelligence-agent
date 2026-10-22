import pytest
from pydantic import ValidationError

from app.models.job import Job


def test_job_accepts_valid_data():
    job = Job(
        title="Junior AI Engineer",
        company="Example Tech",
        required_skills=["Python", "FastAPI"],
        preferred_skills=["Docker", "LLMs"],
        min_years_experience=1,
        location="Remote",
        remote=True,
        description="Build and maintain AI-powered applications.",
    )

    assert job.title == "Junior AI Engineer"
    assert "Python" in job.required_skills
    assert job.remote is True


def test_job_rejects_negative_experience():
    with pytest.raises(ValidationError):
        Job(
            title="AI Engineer",
            company="Example Tech",
            required_skills=["Python"],
            min_years_experience=-1,
            description="Develop AI applications.",
        )


def test_job_requires_at_least_one_required_skill():
    with pytest.raises(ValidationError):
        Job(
            title="AI Engineer",
            company="Example Tech",
            required_skills=[],
            description="Develop AI applications.",
        )
