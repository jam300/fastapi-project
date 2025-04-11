from sqlalchemy.orm import Session
from app.models.post_model import Post
from app.models import Vote
from app.schemas.post_schema import PostCreate
from sqlalchemy import func, text, asc, desc


def get_all_post(user_uuid: str,
                 db: Session,
                 limit: int = 10,
                 skip: int = 0,
                 search: str = "",
                 sort_by:str = "created_at",
                 direction: str = "desc"
                 ) -> list[tuple[Post, int]]:

    query = (
                db.query(Post, func.count(Vote.post_uuid).label("votes"))
                .join(Vote, Vote.post_uuid == Post.uuid, isouter=True)
                .filter(Post.owner_uuid == user_uuid)
                .group_by(Post.uuid)
            )
    if search:
        query = query.filter(
            or_(
                Post.title.ilike(f"%{search}%"),
                Post.content.ilike(f"%{search}%")
            )
        )
    sort_column = text("votes") if sort_by == "votes" else getattr(Post, sort_by, Post.created_at)
    query = query.order_by(asc(sort_column) if direction =="asc" else desc(sort_column))
    return query.offset(skip).limit(limit).all()

def get_post_by_id(user_uuid: str, post_uuid: str, db: Session)  -> tuple[Post, int] | None:
    result = (
        db.query(Post, func.count(Vote.post_uuid).label("votes"))
        .join(Vote, Vote.post_uuid == Post.uuid, isouter=True)
        .filter(Post.owner_uuid == user_uuid, Post.uuid == post_uuid)
        .group_by(Post.uuid)
        .first()
    )
    return result

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