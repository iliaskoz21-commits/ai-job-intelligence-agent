from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_match_endpoint_returns_matching_result():
    payload = {
        "candidate": {
            "name": "Alex",
            "professional_title": "Python Developer",
            "skills": ["Python", "FastAPI", "Git"],
            "years_experience": 2,
        },
        "job": {
            "title": "Backend Developer",
            "company": "Example Tech",
            "required_skills": ["Python", "FastAPI", "Docker"],
            "preferred_skills": ["Git"],
            "min_years_experience": 1,
            "location": "Remote",
            "remote": True,
            "description": "Build backend services.",
        },
    }

    response = client.post("/match", json=payload)

    assert response.status_code == 200

    result = response.json()
    assert result["candidate_name"] == "Alex"
    assert result["job_title"] == "Backend Developer"
    assert result["matched_required_skills"] == ["Python", "FastAPI"]
    assert result["missing_required_skills"] == ["Docker"]
    assert result["matched_preferred_skills"] == ["Git"]
    assert result["required_skill_match_percentage"] == 66.67


def test_match_endpoint_rejects_invalid_candidate():
    payload = {
        "candidate": {
            "name": "Alex",
            "professional_title": "Developer",
            "skills": [],
            "years_experience": 2,
        },
        "job": {
            "title": "Backend Developer",
            "company": "Example Tech",
            "required_skills": ["Python"],
            "description": "Build backend services.",
        },
    }

    response = client.post("/match", json=payload)

    assert response.status_code == 422
