
from app.models.candidate import Candidate
from app.models.job import Job
from app.models.match_result import MatchResult


def normalize_skill(skill: str) -> str:
    """Normalize a skill for case-insensitive comparison."""
    return skill.strip().casefold()


def build_match_summary(
    percentage: float,
    missing_skills: list[str],
    meets_experience: bool,
    candidate_years: float,
    required_years: float,
) -> str:
    """Create an explainable summary from matching results."""

    summary = (
        f"The candidate matches {percentage:.2f}% "
        "of the required skills."
    )

    if missing_skills:
        summary += (
            " Missing required skills: "
            + ", ".join(missing_skills)
            + "."
        )
    else:
        summary += " All required skills are matched."

    if meets_experience:
        summary += (
            f" The candidate meets the experience requirement "
            f"({candidate_years:g} years; "
            f"{required_years:g} required)."
        )
    else:
        summary += (
            f" The candidate does not meet the experience "
            f"requirement ({candidate_years:g} years; "
            f"{required_years:g} required)."
        )

    return summary


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

    percentage = round(
        len(matched_required) / len(job.required_skills) * 100,
        2,
    )

    meets_experience = (
        candidate.years_experience >= job.min_years_experience
    )

    summary = build_match_summary(
        percentage=percentage,
        missing_skills=missing_required,
        meets_experience=meets_experience,
        candidate_years=candidate.years_experience,
        required_years=job.min_years_experience,
    )

    return MatchResult(
        candidate_name=candidate.name,
        job_title=job.title,
        matched_required_skills=matched_required,
        missing_required_skills=missing_required,
        matched_preferred_skills=matched_preferred,
        required_skill_match_percentage=percentage,
        candidate_years_experience=candidate.years_experience,
        required_years_experience=job.min_years_experience,
        meets_experience_requirement=meets_experience,
        match_summary=summary,
    )
