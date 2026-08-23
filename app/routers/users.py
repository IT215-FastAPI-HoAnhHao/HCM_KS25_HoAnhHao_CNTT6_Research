from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_user
from app.dependencies.role import require_admin
from app.models.user import User
from app.schemas.user import UserResponse


router = APIRouter(prefix="/users",tags=["Users"]
)


@router.get("/me", response_model=UserResponse)
def get_my_profile(current_user = Depends(get_current_user)):

    return current_user


@router.get("",response_model=list[UserResponse])
def get_users(search: str | None = None, is_active: bool | None = None, db: Session = Depends(get_db), current_user = Depends(require_admin)):

    query = db.query(User)
    if search:
        query = query.filter((User.full_name.contains(search)) | (User.email.contains(search)))

    if is_active is not None:
        query = query.filter(User.is_active == is_active)

    return query.all()