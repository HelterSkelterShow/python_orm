from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import (DeclarativeBase, Mapped, Session,
                            mapped_column, relationship)


class Base(DeclarativeBase):
    pass
print("")

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(200), unique=True)
    grades: Mapped[list["Grade"]] = relationship(back_populates="student")


class Grade(Base):
    __tablename__ = "grades"

    id: Mapped[int] = mapped_column(primary_key=True)
    course: Mapped[str] = mapped_column(String(100))
    score: Mapped[int]
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    student: Mapped[Student] = relationship(back_populates="grades")


engine = create_engine("sqlite:///college1.db", echo=True)
Base.metadata.create_all(engine)

with Session(engine) as session:
    anna = Student(name="Анна", email="anna@example.com")
    anna.grades = [Grade(course="Python", score=4),
                   Grade(course="SQL", score=4)]
    session.add(anna)
    session.commit()

    stmt = select(Student).where(Student.email == "anna@example.com")
    student = session.scalars(stmt).one()
    for g in student.grades:
        print(student.name, g.course, g.score)
    print("\n\n\n", "=================", "\n", stmt)