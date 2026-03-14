"""Application entry point."""

from fastapi import FastAPI, File, Form, HTTPException, UploadFile

from app.schemas import ReviewRequest, ReviewResult
from app.services.matching import review_resume
from app.services.pdf_extraction import extract_text_from_pdf

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

@app.post("/reviews/pdf", response_model=ReviewResult)
async def create_pdf_review(
    resume: UploadFile = File(...),
    job_description: str = Form(...),
) -> ReviewResult:
    if resume.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Please upload a PDF résumé.",
        )

    try:
        resume_text = extract_text_from_pdf(await resume.read())
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error

    return review_resume(resume_text, job_description)