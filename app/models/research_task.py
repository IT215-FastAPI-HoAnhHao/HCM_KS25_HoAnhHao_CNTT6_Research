from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, null

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


from app.db.database import Base


class ResearchTask(Base):
    __tablename__ = "research_tasks"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("research_project.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    assignee_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    status = Column(String(20), default="TODO", nullable=False)
    priority = Column(String(20), default="MEDIUM", nullable=False)
    due_data = Column(DateTime(timezone=True), nullable=True)
    create_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    project = relationship("ResearchProject", back_populates="tasks")

    assignee = relationship("User", back_populates="assigned_tasks", foreign_keys=[assignee_id])
