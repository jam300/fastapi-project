from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_uuid: str) -> User | None:
    return db.query(User).filter(User.uuid == user_uuid).first()

def get_user_by_email(db: Session, email: str,):
    return db.query(User).filter(User.email == email).first()

def get_all_users(db: Session) -> list[User]:
    return db.query(User).all()

def create_user(db: Session, user_data: UserCreate) -> User:
    new_user = User(**user_data.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def delete_user(user: User, db: Session) -> None:
    db.delete(user)
    db.commit()

