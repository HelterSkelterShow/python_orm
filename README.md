# SQLAlchemy + Alembic Demo

Демонстрационный проект для лекции: слой подключения к БД,
модели, репозиторий и миграции.

## Установка

    python -m venv .venv
    source .venv/bin/activate      # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

## Запуск примеров

    python -m examples.01_orm_minimal
    python -m examples.02_core_tables
    python -m examples.03_raw_sql_injection
    python -m examples.04_transactions
    python -m examples.05_n_plus_one
    python -m examples.06_queries_cheatsheet

## Миграции

    alembic upgrade head
    alembic revision --autogenerate -m "описание"
    alembic downgrade -1