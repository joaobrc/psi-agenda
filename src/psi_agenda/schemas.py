from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    model_config = ConfigDict(from_attributes=True)


class User(UserCreate):
    id: int


class UserDB(UserCreate):
    id: int


class Users(BaseModel):
    usuarios: list[User]


class Profissional(BaseModel):
    nome: str
    numero_conselho: str
    data_desligamento: datetime | None
    model_config = ConfigDict(from_attributes=True)


class Profissionais(BaseModel):
    profissionais: list[Profissional]


class Token(BaseModel):
    access_token: str
    type_token: str
