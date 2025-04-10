from app.database import get_db
from app.services import auth_service

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login")
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    access_token = auth_service.authenticate_user(user_credentials.username, user_credentials.password, db)
    return {"access_token": access_token, "token_type": "bearer"}