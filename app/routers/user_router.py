from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserCreate, UserResponse
from app.services import user_service
from app.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user_by_id(user_id, db)

@router.get("/", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return user_service.get_all_users(db)

@router.post("/", status_code = status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.register_user(user, db)