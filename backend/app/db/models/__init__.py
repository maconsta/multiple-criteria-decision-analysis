from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from os import environ as env

host = env.get("DB_HOST")
user = env.get("DB_USER")
password = env.get("DB_PASSWORD")
database = env.get("DB_DATABASE")
port = env.get("DB_PORT")

url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(
    url,
    pool_pre_ping=True,
    pool_recycle=300
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Model = declarative_base()
metadata = Model.metadata

@contextmanager
def session_scope():
    """
    Provide a transactional scope around a series of operations.

    Usage:
        with session_scope() as db:
            db.add(some_object)
            db.query(YourModel)...
    """
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

from backend.app.db.models.user import User
from backend.app.db.models.project import Project
from backend.app.db.models.task import Task
from backend.app.db.models.alternative import Alternative
from backend.app.db.models.criterion import Criterion
from backend.app.db.models.decision_matrix import DecisionMatrix
from backend.app.db.models.trade_off import TradeOff
