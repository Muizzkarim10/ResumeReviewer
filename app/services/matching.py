"""Deterministic, explainable skill matching.

This is intentionally not AI-generated feedback yet. A rule-based first pass makes
the score inspectable and gives us a baseline to improve with an LLM later.
"""

from app.schemas import ReviewResult

SKILL_PATTERNS: dict[str, tuple[str, ...]] = {
    "Python": ("python",),
    "SQL": ("sql", "postgresql", "mysql", "sqlite"),
    "Machine Learning": ("machine learning", "scikit-learn", "sklearn"),
    "Deep Learning": ("deep learning", "pytorch", "tensorflow", "keras"),
    "Data Analysis": ("data analysis", "pandas", "numpy"),
    "FastAPI": ("fastapi",),
    "Docker": ("docker", "containerization"),
    "Git": ("git", "github", "gitlab"),
    "AWS": ("aws", "amazon web services"),
    "React": ("react", "react.js", "reactjs"),
    "JavaScript": ("javascript", "typescript"),
}


def _skills_in(text: str) -> list[str]:
    lowered_text = text.lower()
    return [
        skill
        for skill, terms in SKILL_PATTERNS.items()
        if any(term in lowered_text for term in terms)
    ]


def review_resume(resume_text: str, job_description: str) -> ReviewResult:
    """Compare recognized skills in the resume with skills requested by the job."""
    requested_skills = _skills_in(job_description)
    resume_skills = set(_skills_in(resume_text))
    matched_skills = [skill for skill in requested_skills if skill in resume_skills]
    missing_skills = [skill for skill in requested_skills if skill not in resume_skills]

    if requested_skills:
        score = round(100 * len(matched_skills) / len(requested_skills))
        note = "Score reflects recognized skills requested in this job description."
    else:
        score = 0
        note = (
            "No supported skills were recognized in the job description yet. "
            "The skill library will expand in a later milestone."
        )

    suggestions = [
        f"If you have real experience with {skill}, add a specific achievement that shows it."
        for skill in missing_skills
    ]
    if not suggestions:
        suggestions.append(
            "Tailor your professional summary to the role and quantify your strongest results."
        )

    return ReviewResult(
        score=score,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        suggestions=suggestions,
        note=note,
    )
