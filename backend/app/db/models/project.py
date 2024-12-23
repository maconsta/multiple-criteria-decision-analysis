from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.dialects import postgresql as pg
from sqlalchemy.orm import Relationship

from backend.app.db.models.base import TimeStampedModel

from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import Column, String


class Project(TimeStampedModel):
    __tablename__ = "projects"

    project_id = Column(Integer, primary_key=True, autoincrement=True)
    project_name = Column(String(70), nullable=False)
    visibility = Column(Boolean, nullable=False)
    collaborators = Column(ARRAY(String), default=list)
    owner = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="Cascade"),
        nullable=False,
        index=True,
    )

    user = Relationship("User", back_populates="projects")
    tasks = Relationship("Task", back_populates="project", passive_deletes=True)

    def __repr__(self):
        return f"{self.__class__.__name__}, project name: {self.project_name}, visibility {self.visibility}, collaborators {self.collaborators}"
