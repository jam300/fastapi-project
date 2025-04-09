from typing import Annotated
from pydantic import BaseModel, Field
from typer import Optional
from datetime import datetime

from app.schemas.user_schema import UserResponse

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse

    class Config:
        orm_mode =True

class PostVote(BaseModel):
    Post: PostResponse
    Votes: int

    class Config:
        orm_mode = True

class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(le=1)]
