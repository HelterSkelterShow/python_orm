"""Шпаргалка по запросам SQLAlchemy 2.0."""
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.base import Base
from app.db.engine import engine
from app.models.student import Student
from app.models.grade import Grade

Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add(Student(name="Анна", email="anna@example.com"))
    session.commit()

with Session(engine) as session:
    # все объекты
    all_students = session.scalars(select(Student)).all()
    print("all:", all_students)

    # один или ошибка
    one = session.scalars(
        select(Student).where(Student.email == "anna@example.com")
    ).one()
    print("one:", one)

    # один или None
    maybe = session.scalars(
        select(Student).where(Student.email == "nobody@example.com")
    ).one_or_none()
    print("one_or_none:", maybe)

    # по первичному ключу
    by_pk = session.get(Student, 1)
    print("get:", by_pk)

    # сортировка и лимит
    top = session.scalars(
        select(Student).order_by(Student.name).limit(10)
    ).all()
    print("limit:", top)

    # join
    rows = session.execute(
        select(Student, Grade).join(Student.grades)
    ).all()
    print("join:", rows)