from app.database import get_db
from app.schemas.post_schema import PostCreate, PostResponse, PostUpdate, PostVoteResponse
from app.services import post_service
from app.utils.oauth2 import get_current_user_uuid

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/post",
    tags=["Posts"]
)

@router.get("/{post_uuid}", response_model = PostVoteResponse)
def get_post(user_uuid:str, post_uuid: str,  db: Session = Depends(get_db)):
    return post_service.get_post_by_id(user_uuid, post_uuid, db)

@router.get("/", response_model=list[PostVoteResponse])
def get_all_posts(user_uuid: str = Depends(get_current_user_uuid),
                  db: Session = Depends(get_db),
                  friend_uuid: str = "",
                  limit: int = 10,
                  skip: int = 0,
                  search: str = "",
                  sort_by: str = "created_at",
                  direction: str = "desc"
                  ):

    return post_service.get_all_post(
        user_uuid=user_uuid,
        db=db,
        friend_uuid=friend_uuid or None,
        limit=limit,
        skip=skip,
        search=search,
        sort_by=sort_by,
        direction=direction
    )

@router.post("/", status_code = status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(post: PostCreate, user_uuid: str = Depends(get_current_user_uuid), db: Session = Depends(get_db)):
    return post_service.create_post(post, user_uuid, db)

@router.put("/{post_uuid}", response_model=PostResponse)
def update_post(post_uuid: str, data: PostUpdate, user_uuid: str = Depends(get_current_user_uuid), db: Session = Depends(get_db)):
    return post_service.update_post(post_uuid, user_uuid, data, db)

@router.delete("/{post_uuid}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_uuid: str,  user_uuid: str = Depends(get_current_user_uuid), db: Session = Depends(get_db)):
    return post_service.delete_post(post_uuid, user_uuid, db)
