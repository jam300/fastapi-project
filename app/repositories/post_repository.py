from sqlalchemy.orm import Session
from app.models.post_model import Post
from app.schemas.post_schema import PostCreate



def get_all_post(user_uuid: str, db: Session) -> list[Post]:
    return  db.query(Post).filter(Post.owner_uuid == user_uuid).all()

def get_post_by_id(user_uuid: str, post_uuid: str, db: Session)  -> Post | None:
    return db.query(Post).filter(Post.owner_uuid == user_uuid, Post.uuid == post_uuid).first()

def get_post_for_vote(post_uuid: str, db: Session)-> Post | None:
    return db.query(Post).filter(Post.uuid == post_uuid).first()

def create_post(post: PostCreate, user_uuid: str, db: Session) -> Post | None:
    new_post = Post(**post.model_dump(), owner_uuid = user_uuid)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def update_post(post: Post, updates: dict, db: Session) -> Post:
    for key, value in updates.items():
        setattr(post, key, value)
    db.commit()
    db.refresh(post)
    return post

def delete_post(post: Post, db: Session) -> None:
    db.delete(post)
    db.commit()