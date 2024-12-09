from fastapi import FastAPI, Depends
from app.routes.course_routes import router as course_router
from app.db.models import MongoDB
from app.config import MONGO_URI, MONGO_DB_NAME

app = FastAPI()

# MongoDB setup
db = MongoDB(MONGO_URI, MONGO_DB_NAME)

# Routes
app.include_router(course_router)
