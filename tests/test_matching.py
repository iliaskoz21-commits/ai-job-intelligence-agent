from app.models.candidate import Candidate
from app.models.job import Job
from app.services.matching import match_candidate_to_job


def test_matching_calculates_required_skill_coverage():
    candidate = Candidate(
        name="Alex",
        professional_title="Python Developer",
        skills=["Python", "FastAPI", "Git"],
        years_experience=2,
    )

    job = Job(
        title="Backend Developer",
        company="Example Tech",
        required_skills=["Python", "FastAPI", "Docker"],
        preferred_skills=["Git", "SQL"],
        description="Build backend services.",
    )

    result = match_candidate_to_job(candidate, job)

    assert result.matched_required_skills == ["Python", "FastAPI"]
    assert result.missing_required_skills == ["Docker"]
    assert result.matched_preferred_skills == ["Git"]
    assert result.required_skill_match_percentage == 66.67


def test_matching_is_case_insensitive():
    candidate = Candidate(
        name="Alex",
        professional_title="Developer",
        skills=["PYTHON", " fastapi "],
        years_experience=1,
    )

    job = Job(
        title="Developer",
        company="Example Tech",
        required_skills=["Python", "FastAPI"],
        description="Develop applications.",
    )

    result = match_candidate_to_job(candidate, job)

    assert result.required_skill_match_percentage == 100.0


def test_matching_returns_zero_when_no_required_skills_match():
    candidate = Candidate(
        name="Alex",
        professional_title="Designer",
        skills=["Photoshop"],
        years_experience=1,
    )

    job = Job(
        title="Backend Developer",
        company="Example Tech",
        required_skills=["Python", "Docker"],
        description="Build backend services.",
    )

    result = match_candidate_to_job(candidate, job)

    assert result.required_skill_match_percentage == 0.0
    assert result.missing_required_skills == ["Python", "Docker"]


def test_matching_detects_insufficient_experience():
    candidate = Candidate(
        name="Alex",
        professional_title="Python Developer",
        skills=["Python"],
        years_experience=2,
    )

    job = Job(
        title="Senior Python Developer",
        company="Example Tech",
        required_skills=["Python"],
        min_years_experience=3,
        description="Develop backend services.",
    )

    result = match_candidate_to_job(candidate, job)

    assert result.candidate_years_experience == 2
    assert result.required_years_experience == 3
    assert result.meets_experience_requirement is False


def test_matching_accepts_exact_experience_requirement():
    candidate = Candidate(
        name="Alex",
        professional_title="Python Developer",
        skills=["Python"],
        years_experience=3,
    )

    job = Job(
        title="Python Developer",
        company="Example Tech",
        required_skills=["Python"],
        min_years_experience=3,
        description="Develop backend services.",
    )

    result = match_candidate_to_job(candidate, job)

    assert result.meets_experience_requirement is True

def test_matching_summary_explains_missing_skills_and_experience():
    candidate = Candidate(
        name="Alex",
        professional_title="Python Developer",
        skills=["Python", "FastAPI"],
        years_experience=2,
    )

    job = Job(
        title="Backend Developer",
        company="Example Tech",
        required_skills=["Python", "FastAPI", "Docker"],
        min_years_experience=3,
        description="Build backend services.",
    )

    result = match_candidate_to_job(candidate, job)

    assert "66.67%" in result.match_summary
    assert "Docker" in result.match_summary
    assert "does not meet the experience requirement" in result.match_summary

	
