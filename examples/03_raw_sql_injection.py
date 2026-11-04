"""Сырой SQL: f-строка vs параметр :login."""
from sqlalchemy import create_engine, text

engine = create_engine("sqlite://")

with engine.begin() as conn:
    conn.execute(text("CREATE TABLE users (login TEXT, role TEXT)"))
    conn.execute(text(
        "INSERT INTO users VALUES ('anna', 'admin'), ('boris', 'user')"
    ))

login = "x' OR '1'='1"  # строка пришла от пользователя

with engine.connect() as conn:
    bad = conn.execute(
        text(f"SELECT login, role FROM users WHERE login = '{login}'")
    )
    print("f-строка:", bad.all())

    good = conn.execute(
        text("SELECT login, role FROM users WHERE login = :login"),
        {"login": login},
    )
    print("параметр:", good.all())