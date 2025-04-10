from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.repositories import post_repository
from app.schemas.post_schema import PostCreate, PostUpdate
from app.models import Post

def get_all_post(user_uuid: str, db: Session) -> list[Post]:
    return post_repository.get_all_post(user_uuid, db)

def get_post_by_id(user_uuid: str, post_uuid: str, db: Session) -> Post | None:
    post = post_repository.get_post_by_id(user_uuid, post_uuid, db)

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found."
        )

    return post

def create_post(post: PostCreate, user_uuid: str, db: Session) -> Post | None:
    return  post_repository.create_post(post, user_uuid, db)

def update_post(post_uuid: str, user_uuid: str, data: PostUpdate, db: Session) -> Post:
    post = post_repository.get_post_by_id(user_uuid, post_uuid, db)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found."
        )

    if post.owner_uuid != user_uuid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to update this post."
        )

    return post_repository.update_post(post, data.model_dump(exclude_unset=True), db)

def delete_post(post_uuid: str, user_uuid:str, db: Session) -> None:
    post = post_repository.get_post_by_id(user_uuid, post_uuid, db)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found."
        )

    if post.owner_uuid != user_uuid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to delete this post."
        )

    post_repository.delete_post(post, db)