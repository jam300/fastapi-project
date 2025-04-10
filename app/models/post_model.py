from app.database import Base
from sqlalchemy import Column, Integer, String,  Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy import DateTime
import uuid

class Post(Base):
    __tablename__ = "posts"

    uuid = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    title = Column(String(150), nullable=False)
    content = Column(String(2000), nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text('GETDATE()'))
    owner_uuid = Column(String(36), ForeignKey("users.uuid", name="fk_posts_owner_uuid", ondelete="CASCADE"), index=True, nullable=False)
    owner = relationship("User", back_populates="posts")
    votes = relationship("Vote", back_populates="post", cascade="all, delete-orphan")