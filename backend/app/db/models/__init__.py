from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from os import environ as env

#db config vars
host = env.get("DB_HOST")
user = env.get("DB_USER")
password = env.get("DB_PASSWORD")
database = env.get("DB_DATABASE")
port = env.get("DB_PORT")

url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(url, pool_pre_ping=True)

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Model = declarative_base()
Model.query = session.query_property()
metadata = Model.metadata

from backend.app.db.models.user import User
from backend.app.db.models.project import Project
from backend.app.db.models.task import Task
from backend.app.db.models.alternative import Alternative
from backend.app.db.models.criterion import Criterion
from backend.app.db.models.decision_matrix import DecisionMatrix
from backend.app.db.models.trade_off import TradeOff

