from fastapi import FastAPI

from app.db.database import Base, engine
from app.models.user import User
from app.models.research_project import ResearchProject, ResearchMember
from app.models.research_task import ResearchTask
from app.routers.health import router as health_router
from app.core.exceptions import register_exception_handlers

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


@app.get("/")
def root():
    return {
        "message": "Research Group Management API is running"
    }
