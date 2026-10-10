from collections.abc import Generator

from sqlalchemy.orm import Session

from app.db.session import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """Disponibiliza uma sessão e a fecha ao terminar a requisição."""
    with SessionLocal() as session:
        yield session
