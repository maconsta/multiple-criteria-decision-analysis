from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from os import environ as env

#db config vars
host = env.get("host")
user = env.get("user")
password = env.get("password")
database = env.get("database")
port = env.get("port")

url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(url)

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

