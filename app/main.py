from fastapi import FastAPI

from app.db.database import Base, engine







Base.matedate.create_all(bind=engine)

app = FastAPI(
    title = "Research Group Management API",
    version="1.0.0"
)

