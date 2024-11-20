from sqlalchemy import Column, Integer, String, ForeignKey, REAL
from sqlalchemy.dialects import postgresql as pg
from sqlalchemy.orm import Relationship

from backend.app.db.models.base import TimeStampedModel


class TradeOff(TimeStampedModel):
    __tablename__ = 'trade_offs'

    trade_off_id = Column(Integer, primary_key=True, autoincrement=True)
    criteria_weights = Column(pg.ARRAY(REAL))
    decision_method = Column(String(80))
    normalization_method = Column(String(80))
    task_id = Column(Integer, ForeignKey("tasks.task_id", ondelete="Cascade"), nullable = False, index = True)

    task = Relationship('Task', back_populates='trade_offs')

    # def __repr__(self):
    #     return (f"{self.__class__.__name__}, criterion Name: {self.criterion_name}, beneficiality: {self.min_max}, "
    #             f"description {self.description}")
