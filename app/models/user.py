from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    role = Column(String(20), default="USER", nullable=False)
    is_active = Column(Boolean,default=True, nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)

    # Quan hệ với project mà user sở hữu
    owned_projects = relationship("ResearchProject", back_populates="owner", foreign_keys="ResearchProject.owner_id")

    # Quan hệ với bảng thành viên project
    memberships = relationship("ResearchMember", back_populates="user", cascade="all, delete-orphan")

    # Quan hệ với task được giao
    assigned_tasks = relationship("ResearchTask",back_populates="assignee",foreign_keys="ResearchTask.assignee_id")
