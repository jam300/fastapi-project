from app.repositories import user_repository
from app.utils import hashing, oauth2
from fastapi import HTTPException, status
from sqlalchemy.orm import Session


def authenticate_user(email: str, password: str, db: Session) -> str:
    user = user_repository.get_user_by_email(db, email)
    if not user or not hashing.verify(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials"
        )

    return oauth2.create_access_token(data={"user_uuid": str(user.uuid)})