from sqlalchemy.orm import Session
from app.models.vote_model import Vote

def get_vote(user_uuid: str, post_uuid: str, db: Session) -> Vote | None:
    return db.query(Vote).filter(
        Vote.user_uuid == user_uuid,
        Vote.post_uuid == post_uuid
    ).first()

def add_vote(user_uuid: str, post_uuid: str, db: Session) -> Vote:
    vote = Vote(user_uuid=user_uuid, post_uuid=post_uuid)
    db.add(vote)
    db.commit()
    db.refresh(vote)
    return vote

def remove_vote(vote: Vote, db: Session) -> None:
    db.delete(vote)
    db.commit()