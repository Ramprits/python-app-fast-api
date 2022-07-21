from sqlalchemy.orm import Session
from core.hashing import Hasher
from db.models.users import User

from schemas.users import CreateUser


def create_new_user(user: CreateUser, db: Session):
    user = User(
        username=user.username,
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        first_name=user.first_name,
        last_name=user.last_name
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def fetch_users(db: Session):
    return db.query(User).all()
