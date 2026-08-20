from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, UniqueConstraint, null
from sqlalchemy.orm import relationship
from sqlalchemy.sql import  func

from app.db.database import Base


class ResearchProject(Base):
    __tablename__ = "research_project"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="RESTRICT"), nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


    # Người sở hữu project
    owner = relationship("User", back_populates="owend_projects", foreign_keys=[owner_id])

    # DAnh sách thành viên trong project
    members = relationship("ResearchMember", back_populates="project", cascade="all, delete-orphan")

    # Danh sách task của project
    tasks = relationship("ResearchTask", back_populates="project", cascade="all, delete-orphan")



class ResearchMember(Base):
    __tablename__  = "research_menbers"

    __table_args__ = (UniqueConstraint("project_id", "user_id", name="up_research_member_project_user"),)


    project_id = Column(Integer, ForeignKey("research_project.id", ondelete="CASCADE"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    role = Column(String(20), default="MEMBER", nullable=False)
    joined_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    project = relationship("ResearchProject", back_populates="members")

    user = relationship("User", back_populates="memberships")
