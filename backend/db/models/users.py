from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True, index=True)
    profile_pic = Column(String, nullable=True)
    hashed_password = Column(String, nullable=True)
    is_superuser = Column(Boolean(), default=True)
    is_active = Column(Boolean(), default=True)
    jobs = relationship('Job', back_populates="owner")
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow)
