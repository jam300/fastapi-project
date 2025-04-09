from typing import Annotated
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

from app.schemas.user_schema import UserResponse

class _PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(_PostBase):
    pass

class PostResponse(_PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse

    class Config:
        from_attributes = True

class PostVote(BaseModel):
    Post: PostResponse
    Votes: int

    class Config:
        from_attributes = True

class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(le=1)]
