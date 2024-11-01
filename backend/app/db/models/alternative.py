from sqlalchemy import Column, Integer, String, PickleType, ForeignKey
from sqlalchemy.orm import Relationship
from sqlalchemy.dialects import postgresql as pg

from backend.app.db.models.base import TimeStampedModel


class Alternative(TimeStampedModel):
    __tablename__ = 'alternatives'

    alternative_id = Column(Integer, primary_key=True, autoincrement=True)
    alternative_name = Column(String(80), nullable=False)
    alternative_values = Column(pg.ARRAY(Integer))
    description = Column(String(500))
    task_id = Column(Integer, ForeignKey("tasks.task_id", ondelete="Cascade"), nullable = False, index = True)

    task = Relationship('Task', back_populates='alternatives')
    

    def __repr__(self):
        return (f"{self.__class__.__name__}, alternative name: {self.alternative_name}, values: {self.values}, "
                f"description: {self.description}")
