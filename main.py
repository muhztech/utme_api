from fastapi import FastAPI, Query
import json
import random
import os

# ----------------------------------------
# App Configuration
# ----------------------------------------
app = FastAPI(
    title="UTME Practice API",
    description="Original UTME-style practice questions based on JAMB syllabus",
    version="1.0.0"
)

# ----------------------------------------
# Load Questions at Startup
# ----------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_FILE = os.path.join(BASE_DIR, "utme_practice_questions_original_800.json")

with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
    questions = json.load(f)

# ----------------------------------------
# Root Endpoint
# ----------------------------------------
@app.get("/")
def root():
    return {
        "message": "UTME Practice API is running",
        "total_questions": len(questions)
    }

# ----------------------------------------
# Get All Subjects
# ----------------------------------------
@app.get("/subjects")
def get_subjects():
    """
    Returns all available subjects
    """
    return sorted({q["subject"] for q in questions})

# ----------------------------------------
# Get Random Questions by Subject
# ----------------------------------------
@app.get("/questions")
def get_questions(
    subject: str = Query(..., description="Subject name e.g. Mathematics"),
    limit: int = Query(
        10,
        ge=1,
        le=100,
        description="Number of questions to fetch"
    )
):
    """
    Returns random UTME-style questions filtered by subject
    """
    filtered_questions = [
        q for q in questions
        if q["subject"].lower() == subject.lower()
    ]

    if not filtered_questions:
        return {
            "error": "Subject not found",
            "available_subjects": sorted({q["subject"] for q in questions})
        }

    return random.sample(
        filtered_questions,
        min(limit, len(filtered_questions))
    )
