from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    model_config = ConfigDict(from_attributes=True)


class User(UserCreate):
    id: int


class UserDB(UserCreate):
    id: int


class Users(BaseModel):
    usuarios: list[User]
