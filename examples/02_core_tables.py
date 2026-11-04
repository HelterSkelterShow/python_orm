"""Core: SQL без классов — Table + MetaData + insert/select."""
from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, insert, select)

engine = create_engine("sqlite://")  # база в памяти
metadata = MetaData()
users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("login", String(50), nullable=False, unique=True),
    Column("role", String(20), nullable=False),
)
metadata.create_all(engine)

with engine.begin() as conn:  # commit при выходе, rollback при исключении
    conn.execute(insert(users), [
        {"login": "anna", "role": "admin"},
        {"login": "boris", "role": "user"},
    ])

with engine.connect() as conn:
    rows = conn.execute(select(users.c.login).where(users.c.role == "user"))
    print(rows.all())