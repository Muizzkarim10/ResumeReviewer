"""Application entry point."""

from fastapi import FastAPI

from app.schemas import ReviewRequest, ReviewResult
from app.services.matching import review_resume

app = FastAPI(
    title="AI Resume Reviewer API",
    version="0.1.0",
    description="Analyze resumes against job descriptions.",
)


@app.get("/health", tags=["system"])
def health_check() -> dict[str, str]:
    """Confirm that the service is available."""
    return {"status": "ok"}


@app.post("/reviews", response_model=ReviewResult, tags=["reviews"])
def create_review(payload: ReviewRequest) -> ReviewResult:
    """Analyze a resume against a job description using explainable skill matching."""
    return review_resume(payload.resume_text, payload.job_description)
