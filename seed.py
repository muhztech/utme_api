import json
from db import engine, SessionLocal
from models import Base, Question

Base.metadata.create_all(bind=engine)

db = SessionLocal()

with open("utme_practice_questions_original_800.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

for q in questions:
    db_question = Question(
        subject=q["subject"],
        topic=q["topic"],
        year=q["year"],
        question=q["question"],
        options=q["options"],
        answer=q["answer"],
        explanation=q["explanation"],
    )
    db.add(db_question)

db.commit()
db.close()

print("✅ Database seeded with UTME-style questions")
