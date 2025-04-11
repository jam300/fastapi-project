from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.repositories import post_repository, user_repository
from app.schemas.post_schema import PostCreate, PostUpdate, PostVoteResponse
from app.models import Post

def get_all_post(
    user_uuid: str,
    db: Session,
    friend_uuid: str | None = None,
    limit: int = 10,
    skip: int = 0,
    search: str = "",
    sort_by: str = "created_at",
    direction: str = "desc"
) -> list[PostVoteResponse]:

    if friend_uuid:
        if friend_uuid == user_uuid:
                HTTPException(status_code=400, detail="You're already viewing your own posts.")
        friend = user_repository.get_user_by_id(db, friend_uuid)
        if not friend:
            raise HTTPException(status_code=404, detail="The user you're trying to view does not exist.")

    target_uuid = friend_uuid or user_uuid
    raw_posts = post_repository.get_all_post(
        db=db,
        user_uuid=target_uuid,
        limit=limit,
        skip=skip,
        search=search,
        sort_by=sort_by,
        direction=direction
    )

    return [
        PostVoteResponse(Post=post, Votes=votes)
        for post, votes in raw_posts
    ]

def get_post_by_id(user_uuid: str, post_uuid: str, db: Session)  -> PostVoteResponse | None:
    result = post_repository.get_post_by_id(user_uuid, post_uuid, db)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found."
        )

    post, votes = result
    return PostVoteResponse(Post=post, Votes=votes)

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