# AI Resume Reviewer

An AI-powered web app that compares a candidate's resume against a job description and returns practical, evidence-based feedback.

## What we will build

1. Resume and job-description input
2. Text extraction and validation
3. Transparent skill and keyword match analysis (in progress)
4. AI feedback tailored to the role
5. A polished web interface, saved reviews, and deployment

## First milestone

The API exposes a health check and a first, explainable review endpoint. It finds
skills mentioned in the job description, checks whether the resume mentions them,
and returns a match score and practical suggestions.

## Run locally

Create and activate a virtual environment, install the dependencies, then start the API:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` to see the interactive API documentation.

## Test the review endpoint

Start the server with `uvicorn app.main:app --reload`, then use the `/docs` page to
send a `POST` request to `/reviews`. Use plain text for now; PDF upload comes next.
