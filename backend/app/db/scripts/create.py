from backend.app.db.models import engine
from backend.app.db.models import Model

from backend.app.db.models.user import User
from backend.app.db.models.alternative import Alternative
from backend.app.db.models.criterion import Criterion
from backend.app.db.models.decision_matrix import DecisionMatrix
from backend.app.db.models.project import Project
from backend.app.db.models.task import Task

Model.metadata.create_all(engine)
