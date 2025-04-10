from app.database import get_db
from app.schemas.post_schema import VoteCreate
from app.services import vote_service
from app.utils.oauth2 import get_current_user_uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/vote",
    tags=["Votes"]
)

@router.post("/")
def vote(data: VoteCreate, user_uuid: str = Depends(get_current_user_uuid), db: Session = Depends(get_db)):
    return {"message": vote_service.create_vote(user_uuid, data.post_uuid, data.dir, db)}