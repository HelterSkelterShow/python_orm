from sqlalchemy import ForeignKey, String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class Grade(Base):
    __tablename__ = "grades"

    id: Mapped[int] = mapped_column(primary_key=True)
    course: Mapped[str] = mapped_column(String(100))
    score: Mapped[int]
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))

    student: Mapped["Student"] = relationship(back_populates="grades")

    def __repr__(self) -> str:
        return f"<Grade id={self.id} course={self.course!r} score={self.score}>"