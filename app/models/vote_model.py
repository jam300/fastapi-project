from sqlalchemy import Column, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from app.database import Base

class Vote(Base):
    __tablename__ = "votes"

    user_uuid = Column(String(36), ForeignKey("users.uuid", name="fk_votes_user_uuid", ondelete="NO ACTION"), primary_key=True)
    post_uuid = Column(String(36), ForeignKey("posts.uuid", name="fk_votes_post_uuid", ondelete="CASCADE"), primary_key=True)

    user = relationship("User", back_populates="votes")
    post = relationship("Post", back_populates="votes")

    __table_args__ = (
        PrimaryKeyConstraint("user_uuid", "post_uuid", name="pk_votes"),
    )
