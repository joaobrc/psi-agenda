from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import get_db
from .models import User
from .schemas import User as schema_use
from .schemas import UserCreate
from .schemas import Users as schema_users

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def hello_world():
    return """
    <html>
        <head>
            <title>Hello World</title>
        </head>
        <body>
            <h1>Hello World</h1>
        </body>
    </html>
    """


@app.post('/user', response_model=schema_use, status_code=HTTPStatus.CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    print(user.email)
    usuario_cadastrado = db.scalar(
        select(User).where(User.email == user.email)
    )
    if usuario_cadastrado:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail='Usuario já cadastrado'
        )
    usuario = User(
        username=user.username, password=user.password, email=user.email
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario


@app.get('/users', response_model=schema_users, status_code=HTTPStatus.OK)
def get_users(db: Session = Depends(get_db)):
    usuarios = db.scalars(select(User)).all()
    return {'usuarios': usuarios}
