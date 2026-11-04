# ВАЖНО: импорт всех моделей нужен для Alembic --autogenerate
from app.models.student import Student
from app.models.grade import Grade

__all__ = ["Student", "Grade"]