from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .schemas import User, UserCreate, Users

app = FastAPI()
usuarios = []


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


@app.post('/user', response_model=User, status_code=HTTPStatus.CREATED)
def create_user(user: UserCreate):
    user = {
        'id': len(usuarios) + 1,
        'name': user.name,
        'email': user.email,
        'password': user.password,
    }
    usuarios.append(user)
    return user


@app.get('/users', response_model=Users, status_code=HTTPStatus.OK)
def get_users():
    return {'usuarios': usuarios}
