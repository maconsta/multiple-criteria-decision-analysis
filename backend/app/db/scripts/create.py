# RUN THIS SCRIPT TO CREATE A DB

from backend.app.db.models import engine
from backend.app.db.models import Model

from backend.app.db.models import (
    User,
    Alternative,
    Criterion,
    DecisionMatrix,
    Project,
    Task,
    TradeOff,
)

Model.metadata.create_all(engine)
