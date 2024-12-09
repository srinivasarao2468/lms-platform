from fastapi import APIRouter, Depends, HTTPException
from app.db.models import MongoDB
from app.services.course_service import CourseService
from app.auth.keycloak_auth import KeycloakAuth
from app.config import KEYCLOAK_SERVER_URL, KEYCLOAK_REALM_NAME, KEYCLOAK_CLIENT_ID, KEYCLOAK_CLIENT_SECRET

router = APIRouter(prefix="/courses")

keycloak_auth = KeycloakAuth(KEYCLOAK_SERVER_URL, KEYCLOAK_REALM_NAME, KEYCLOAK_CLIENT_ID, KEYCLOAK_CLIENT_SECRET)

def get_current_user(token: str):
    user_info = keycloak_auth.get_user_info(token)
    if not user_info:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user_info

@router.get("/")
def get_courses(db: MongoDB = Depends(), user=Depends(get_current_user)):
    return CourseService(db).get_all_courses()
