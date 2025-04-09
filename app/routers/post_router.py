from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas.post_schema import PostCreate, PostResponse
from app.services import post_service
from app.database import get_db


router = APIRouter(
    prefix="/post",
    tags=["Posts"]
)

@router.get("/{post_id}", response_model=PostResponse)
def get_post(user_id:int, post_id: int,  db: Session = Depends(get_db)):
    return post_service.get_post_by_id(user_id, post_id, db)

@router.get("/", response_model=list[PostResponse])
def get_all_posts(user_id: int, db: Session = Depends(get_db)):
    return post_service.get_all_post(user_id, db)

@router.post("/", status_code = status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(post: PostCreate, user_id:int, db: Session = Depends(get_db)):
    return post_service.create_post(post, user_id, db)