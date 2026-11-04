"""Минимальный полный пример ORM с использованием репозитория."""
from sqlalchemy import select
from sqlalchemy.orm import Session

import sys
import os

from app.db.base import Base
from app.db.engine import engine
from app.models.student import Student
from app.models.grade import Grade
from app.repositories.student_repository import StudentRepository

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

Base.metadata.create_all(engine)

#Создаём сессию, открываем транзакцию и передаём сессию в репозиторий
with Session(engine) as session, session.begin():
    repo = StudentRepository(session)
    
    anna = Student(name="Анна", email="anna@example2.com")
    anna.grades = [
        Grade(course="Python", score=5),
        Grade(course="SQL", score=4),
    ]
    
    repo.add(anna)

with Session(engine) as session:
    repo = StudentRepository(session)
    
    student = repo.get_by_email("anna@example.com")
    
    if student:
        for g in student.grades:
            print(student.name, g.course, g.score)