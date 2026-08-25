from colorama import deinit
from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.research_project import ResearchMemberCreate, ResearchMemberResponse, ResearchProjectCreate, ResearchProjectResponse
from app.services.research_project_service import add_research_member, create_research_project, get_research_projects, get_research_project, update_research_project, delete_research_project, get_research_members



router = APIRouter(prefix="/research-projects", tags=["Researcg Projects"])


@router.post("", response_model=ResearchProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(project_data: ResearchProjectCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = create_research_project(
        project_data=project_data,
        owner_id=current_user.id,
        db=db
    )

    return project


@router.get("",response_model=list[ResearchProjectResponse])
def get_projects(search: str | None = None, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):

    projects = get_research_projects(
        user_id = current_user.id,
        search=search,
        db=db
    )

    return projects

@router.get("/{project_id}", response_model=ResearchProjectResponse)
def get_project(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = get_research_project(
        project_id = project_id,
        user_id= current_user.id,
        db=db
    )

    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Không tìm thấy dự án nghiên cứu")


    return project


@router.patch("/{project_id}", response_model=ResearchProjectResponse)
def update_project(project_id: int, project_data: ResearchProjectResponse, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):

    project = update_research_project(
        project_id=project_id,
        project_data=project_data,
        user_id=current_user.id,
        db=db
    )

    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Không tìm thấy dự án nghiên cứu")

    if project == "FORBIDDEN":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Chỉ chủ sở hữu mới có thể cập nhật dự án nghiên cứu")


    return project


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = delete_research_project(
        project_id=project_id,
        user_id=current_user.id,
        db=db
    )

    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Không tìm thấy dự án nghiên cứu")

    if result == "FORBIDDEN":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Chỉ chủ sở hữu mới có thể xóa dự án nghiên cứu")

    

@router.post("/{project_id}/members", response_model=ResearchMemberResponse, status_code=status.HTTP_201_CREATED)
def add_member(project_id: int, member_data: ResearchMemberCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    member = add_research_member(
        project_id=project_id,
        member_data=member_data,
        owner_id=current_user.id,
        db=db
    )

    if member is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Không tìm thấy dự án nghiên cứu")

    if member == "FORBIDDEN":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Chỉ chủ sở hữu mới có thể thêm thành viên.")

    if member == "USER_NOT_FOUND":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Không tìm thấy người dùng.")

    if member == "MEMBER_EXISTS":
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Người dùng đã là thành viên")

    return member


@router.get("/{project_id}/members", response_model=list[ResearchMemberResponse])
def get_members(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    members = get_research_members(
        project_id=project_id,
        user_id=current_user.id,
        db=db
    )

    if members is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Không tìm thấy dự án nghiên cứu")

    if members == "FORBIDDEN":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Chỉ các thành viên dự án mới có thể xem danh sách thành viên.")

    return members