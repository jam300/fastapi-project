from app.database import get_db
from app.schemas.user_schema import UserCreate, UserResponse
from app.services import user_service

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/{user_uuid}", response_model=UserResponse)
def get_user(user_uuid: str, db: Session = Depends(get_db)):
    return user_service.get_user_by_id(user_uuid, db)

@router.get("/", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return user_service.get_all_users(db)

@router.post("/", status_code = status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.register_user(user, db)

@router.delete("/{user_uuid}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_uuid: str, db: Session = Depends(get_db)):
    return user_service.delete_user(user_uuid, db)