from app.database import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import uuid


class User(Base):
    __tablename__ = "users"

    uuid = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)

    posts = relationship("Post", back_populates="owner", cascade="all, delete-orphan")
    votes = relationship("Vote", back_populates="user", cascade="all, delete-orphan")