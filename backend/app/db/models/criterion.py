from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import Relationship
from sqlalchemy.dialects import postgresql as pg

from backend.app.db.models.base import TimeStampedModel


class Criterion(TimeStampedModel):
    __tablename__ = 'criteria'

    criterion_id = Column(Integer, primary_key=True, autoincrement=True)
    criterion_name = Column(String(80), nullable=False)
    criterion_type = Column(String(80), nullable=False)
    min_max = Column(String(3), nullable=False)
    alternatives_values = Column(pg.ARRAY(Numeric))
    alternatives_values_raw = Column(pg.ARRAY(Numeric))
    description = Column(String(500))
    preference_function = Column(String(80))
    q_value = Column(Numeric)
    p_value = Column(Numeric)
    task_id = Column(Integer, ForeignKey("tasks.task_id", ondelete="Cascade"), nullable = False, index = True)

    task = Relationship('Task', back_populates='criteria')


    def __repr__(self):
        return (f"{self.__class__.__name__}, criterion Name: {self.criterion_name}, beneficiality: {self.min_max}, "
                f"description {self.description}")

