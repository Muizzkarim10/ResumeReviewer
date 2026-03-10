"""Request and response shapes for the review API."""

from pydantic import BaseModel, Field


class ReviewRequest(BaseModel):
    resume_text: str = Field(min_length=30, description="Plain text extracted from a resume.")
    job_description: str = Field(
        min_length=30, description="Plain text from the target job description."
    )


class ReviewResult(BaseModel):
    score: int = Field(ge=0, le=100)
    matched_skills: list[str]
    missing_skills: list[str]
    suggestions: list[str]
    note: str
