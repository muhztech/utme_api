from sqlalchemy import Column, Integer, String, Text, JSON
from db import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String, index=True)
    topic = Column(String, index=True)
    year = Column(Integer, index=True)
    question = Column(Text)
    options = Column(JSON)
    answer = Column(String)
    explanation = Column(Text)
