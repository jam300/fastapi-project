from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories import vote_repository
from app.repositories import post_repository

def create_vote(user_uuid: str, post_uuid: str, direction: int, db: Session) -> str:
    post = post_repository.get_post_for_vote(post_uuid, db)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found.")

    existing_vote = vote_repository.get_vote(user_uuid, post_uuid, db)

    if direction == 1:
        if existing_vote:
            raise HTTPException(status_code=409, detail="You already voted on this post.")
        vote_repository.add_vote(user_uuid, post_uuid, db)
        return "Vote registered."

    else:
        if not existing_vote:
            raise HTTPException(status_code=404, detail="Vote not found.")
        vote_repository.remove_vote(existing_vote, db)
        return "Vote removed."