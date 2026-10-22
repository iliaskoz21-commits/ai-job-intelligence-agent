import pytest
from pydantic import ValidationError

from app.models.candidate import Candidate


def test_candidate_accepts_valid_data():
    candidate = Candidate(
        name="Alex",
        professional_title="AI Engineer",
        skills=["Python", "FastAPI", "LLMs"],
        years_experience=3,
        education=["BSc Computer Science"],
    )

    assert candidate.name == "Alex"
    assert "Python" in candidate.skills
    assert candidate.years_experience == 3
    assert candidate.preferred_locations == []


def test_candidate_rejects_negative_experience():
    with pytest.raises(ValidationError):
        Candidate(
            name="Alex",
            professional_title="AI Engineer",
            skills=["Python"],
            years_experience=-1,
        )


def test_candidate_requires_at_least_one_skill():
    with pytest.raises(ValidationError):
        Candidate(
            name="Alex",
            professional_title="AI Engineer",
            skills=[],
            years_experience=1,
        )
