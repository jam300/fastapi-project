from typing import Annotated
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

from app.schemas.user_schema import UserResponse

class _PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(_PostBase):
    pass

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None

    model_config = ConfigDict(from_attributes=True)

class PostResponse(_PostBase):
    uuid: str
    created_at: datetime
    owner_uuid: str
    owner: UserResponse

    model_config = ConfigDict(from_attributes=True)

class PostVoteResponse(BaseModel):
    Post: PostResponse
    Votes: int

    model_config = ConfigDict(from_attributes=True)

class VoteCreate(BaseModel):
    post_uuid: str
    dir: Annotated[int, Field(le=1)]
