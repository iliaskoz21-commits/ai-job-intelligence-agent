
from app.models.candidate import Candidate
from app.models.job import Job
from app.models.match_result import MatchResult


def normalize_skill(skill: str) -> str:
    """Normalize a skill for case-insensitive comparison."""
    return skill.strip().casefold()


def match_candidate_to_job(
    candidate: Candidate,
    job: Job,
) -> MatchResult:
    """Compare candidate skills and experience with job requirements."""

    candidate_skills = {
        normalize_skill(skill): skill
        for skill in candidate.skills
    }

    matched_required = [
        skill
        for skill in job.required_skills
        if normalize_skill(skill) in candidate_skills
    ]

    missing_required = [
        skill
        for skill in job.required_skills
        if normalize_skill(skill) not in candidate_skills
    ]

    matched_preferred = [
        skill
        for skill in job.preferred_skills
        if normalize_skill(skill) in candidate_skills
    ]

    percentage = (
        len(matched_required) / len(job.required_skills) * 100
    )

    meets_experience = (
        candidate.years_experience >= job.min_years_experience
    )

    return MatchResult(
        candidate_name=candidate.name,
        job_title=job.title,
        matched_required_skills=matched_required,
        missing_required_skills=missing_required,
        matched_preferred_skills=matched_preferred,
        required_skill_match_percentage=round(percentage, 2),
        candidate_years_experience=candidate.years_experience,
        required_years_experience=job.min_years_experience,
        meets_experience_requirement=meets_experience,
    )
