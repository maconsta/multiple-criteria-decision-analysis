from sqlalchemy import Column, Integer, String, PickleType, ForeignKey
from sqlalchemy.dialects import postgresql as pg
from sqlalchemy.orm import Relationship

from backend.app.db.models.base import TimeStampedModel


class Task(TimeStampedModel):
    __tablename__ = 'tasks'

    task_id = Column(Integer, primary_key=True, autoincrement=True)
    task_name = Column(String(70), nullable=False)
    method = Column(String(70))
    decision_matrix = Column(PickleType)
    project_id = Column(Integer, ForeignKey("projects.project_id", ondelete="Cascade"), nullable=False, index=True)

    project = Relationship("Project", back_populates="tasks")
    alternatives = Relationship("Alternative", back_populates="task", passive_deletes=True)
    criteria = Relationship("Criterion", back_populates="task", passive_deletes=True)

    # ranking = Column(PickleType) # is this needed ?

    def __repr__(self):
        return (f"{self.__class__.__name__}, task name: {self.task_name}, method: {self.method}, "
                f"decision matrix: {self.decision_matrix}")
