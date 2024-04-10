from datetime import datetime

from sqlalchemy import Column, DateTime

from backend.app.db.models import Model


class TimeStampedModel(Model):
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
