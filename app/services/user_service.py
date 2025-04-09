from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.schemas.user_schema import UserCreate
from app.repositories import user_repository
from app.utils import hashing


def get_user_by_id(user_id: int, db: Session):
    user = user_repository.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user


def get_all_users(db: Session):
    return user_repository.get_all_users(db)

def register_user(user_data: UserCreate, db: Session):
    # Check if the user already exists
    existing_user = user_repository.get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    # Hash the password before saving
    user_data.password = hashing.hash(user_data.password)

    # Create and return the user
    return user_repository.create_user(db, user_data)