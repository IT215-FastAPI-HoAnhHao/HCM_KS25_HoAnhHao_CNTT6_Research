from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.auth_services import register_user

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    new_user = register_user(db=db, user_data=user_data)

    if new_user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email đã tồn tại")
    return new_user
