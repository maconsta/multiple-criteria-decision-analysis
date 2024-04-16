from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects import postgresql as pg

from backend.app.db.models.base import TimeStampedModel


class DecisionMatrix(TimeStampedModel):
    __tablename__ = 'decision_matrix'

    matrix_id = Column(Integer, primary_key=True, autoincrement=True)
    criteria = Column(pg.ARRAY(Integer))  # array of criteria IDs
    alternatives = Column(pg.ARRAY(Integer))  # array of alternatives IDs
    normalization_method = Column(String(80))

    # def __repr__(self):
    #     return (f"{self.__class__.__name__}, criterion Name: {self.criterion_name}, beneficiality: {self.min_max}, "
    #             f"description {self.description}")
