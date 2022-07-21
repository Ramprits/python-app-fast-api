from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.models.users import User
from schemas.users import CreateUser, ShowUser
from db.session import get_db
from db.repository.user import create_new_user, fetch_users
router = APIRouter()


@router.get("/", response_model=List[ShowUser])
def fetch_all_users(db: Session = Depends(get_db)):
    return fetch_users(db)


@router.post("/register", response_model=ShowUser)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    return create_new_user(user, db)
