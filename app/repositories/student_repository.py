from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from app.models.student import Student

class StudentRepository:
    """
    Репозиторий НЕ вызывает commit() — это ответственность вызывающего кода
    (Unit of Work). Так несколько операций можно объединить в одну транзакцию.
    """

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(self, student_id: int) -> Student | None:
        return self.session.get(Student, student_id)

    def get_by_email(self, email: str) -> Student | None:
        stmt = select(Student).where(Student.email == email)
        return self.session.scalars(stmt).one_or_none()

    def get_all(self) -> list[Student]:
        stmt = select(Student)
        return list(self.session.scalars(stmt))

    def get_all_with_grades(self) -> list[Student]:
        # selectinload решает проблему N+1
        stmt = select(Student).options(selectinload(Student.grades))
        return list(self.session.scalars(stmt))

    def add(self, student: Student) -> None:
        self.session.add(student)

    def delete(self, student: Student) -> None:
        self.session.delete(student)