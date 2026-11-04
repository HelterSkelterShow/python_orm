"""Проблема N+1 и её решение через selectinload."""
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.db.base import Base
from app.db.engine import engine
from app.models.student import Student
from app.models.grade import Grade

Base.metadata.create_all(engine)

# Подготовка данных
with Session(engine) as session:
    for i in range(4):
        s = Student(name=f"Студент {i}", email=f"student{i}@example.com")
        s.grades = [Grade(course="Python", score=5),
                    Grade(course="SQL", score=4)]
        session.add(s)
    session.commit()

# Плохо: N+1 — один запрос на студентов и по одному на grades каждого
with Session(engine) as session:
    students = list(session.scalars(select(Student)))
    for s in students:
        print(s.name, [g.course for g in s.grades])   # каждая s.grades — новый запрос

# Хорошо, т.к. вместо lazy load мы применили selectinload -> выполнили 2 запроса вместо N+1
with Session(engine) as session:
    stmt = select(Student).options(selectinload(Student.grades))
    students = list(session.scalars(stmt))
    for s in students:
        print(s.name, [g.course for g in s.grades])