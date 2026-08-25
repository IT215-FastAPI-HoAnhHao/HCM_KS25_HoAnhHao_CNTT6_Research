from fastapi import FastAPI

from app.db.database import Base, engine,SessionLocal
from app.models.user import User
from app.models.research_project import ResearchProject, ResearchMember
from app.models.research_task import ResearchTask
from app.routers.health import router as health_router
from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.core.exceptions import register_exception_handlers
from app.core.security import hash_password
from app.services import research_project_service
from app.routers.research_project import router as research_project_router
# Tạo các bảng trong database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Research Group Management API",
    version="1.0.0"
)

# Đăng ký xử lý exception
register_exception_handlers(app)

# Đăng ký router
app.include_router(health_router)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(research_project_router)

@app.get("/")
def root():
    return {
        "message": "Research Group Management API is running"
    }


def create_admin():
    db = SessionLocal()
    admin = db.query(User).filter(
        User.email == "admin@gmail.com"
    ).first()

    if admin is None:

        admin = User(
            email="admin@gmail.com",
            full_name="hoanhhao",
            password_hash=hash_password("123456"),
            role="ADMIN",
            is_active=True
        )

        db.add(admin)
        db.commit()

    db.close()


create_admin()