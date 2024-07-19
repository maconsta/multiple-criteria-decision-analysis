from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

from backend.app.db.db_config import db_config

url = f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
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
