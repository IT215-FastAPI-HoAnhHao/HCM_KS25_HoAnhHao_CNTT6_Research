from fastapi import Depends, HTTPException, status

from app.dependencies.auth import get_current_user


def require_admin(current_user = Depends(get_current_user)):

    if current_user.role != "ADMIN":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Yêu cầu quyền quản trị viên")

    return current_user