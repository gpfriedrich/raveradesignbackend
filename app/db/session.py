from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import get_settings

# create_engine configura o pool; a conexão só abre na primeira operação SQL.
engine = create_engine(str(get_settings().database_url), pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
