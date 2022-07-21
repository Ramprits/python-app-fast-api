from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str


class ShowUser(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: str

    class Config:
        orm_mode = True
