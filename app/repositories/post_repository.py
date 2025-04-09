from sqlalchemy.orm import Session
from app.models.post_model import Post
from app.schemas.post_schema import PostCreate



def get_all_post(user_id: int, db: Session) -> list[Post]:
    return  db.query(Post).filter(Post.owner_id == user_id).all()

def get_post_by_id(user_id: int, post_id: int, db: Session)  -> Post | None:
    return db.query(Post).filter(Post.owner_id == user_id, Post.id == post_id).first()

def create_post(post: PostCreate, user_id: int, db: Session) -> Post | None:
    new_post = Post(**post.model_dump(), owner_id = user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def update_post():
    pass

def delete_post():
    pass