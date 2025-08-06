# usar fastapi, y dependencias
from fastapi import APIRouter, Depends
from app.schemas.user import User, UserCreate
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.api.controllers import user as user_controller

router = APIRouter(prefix="/users", tags=["Usuarios"])


@router.get(
    "/",
)  # <- definimos el metodo
def get_users():  # <- definimos una funcion
    return [{"id": 1, "name": "Alice"}]  # <- retornando algo


@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_controller.create_user(db, user)
