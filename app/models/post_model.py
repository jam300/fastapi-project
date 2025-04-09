from sqlalchemy import Column, Integer, String,  Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy import DateTime
from app.database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(150), nullable=False)
    content = Column(String(2000), nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, server_default=text('GETDATE()'))
    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")