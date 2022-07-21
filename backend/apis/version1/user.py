from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.users import CreateUser, ShowUser
from db.session import get_db
from db.repository.user import create_new_user
router = APIRouter()


@router.post("/register", response_model=ShowUser)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    return create_new_user(user, db)
