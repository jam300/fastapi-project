from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.repositories import post_repository
from app.schemas.post_schema import PostCreate
from app.models import Post

def get_all_post(user_id: int, db: Session) -> list[Post]:
    return post_repository.get_all_post(user_id, db)

def get_post_by_id(user_id: int, post_id: int, db: Session) -> Post | None:
    post = post_repository.get_post_by_id(user_id, post_id, db)

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found."
        )

    return post

def create_post(post: PostCreate, user_id: int, db: Session) -> Post | None:
    return  post_repository.create_post(post, user_id, db)