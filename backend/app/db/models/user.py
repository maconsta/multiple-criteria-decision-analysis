from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Relationship

from backend.app.db.models.base import TimeStampedModel


class User(TimeStampedModel):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(35), nullable=False)
    last_name = Column(String(35), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(128), nullable=False)

    projects = Relationship("Project", back_populates="user", passive_deletes=True)

    def __repr__(self):
        return f"{self.__class__.__name__}, name: {self.first_name} {self.last_name}, email: {self.email}"
