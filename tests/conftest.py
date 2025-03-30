import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from src.psi_agenda.app import app
from src.psi_agenda.database import get_db
from src.psi_agenda.models import User, table_registro
from src.psi_agenda.security import atribuir_hash


@pytest.fixture
def cliente(sessao_sql):
    def get_session_override():
        return sessao_sql

    with TestClient(app) as client:
        app.dependency_overrides[get_db] = get_session_override
        yield client
    app.dependency_overrides.clear()


@pytest.fixture
def sessao_sql():
    engine_sql = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    table_registro.metadata.create_all(engine_sql)
    with Session(engine_sql) as sessao_sql:
        yield sessao_sql
    table_registro.metadata.drop_all(engine_sql)


@pytest.fixture
def usuario_teste(sessao_sql):
    passwd_teste = '123456'
    usuario_cad_teste = User(
        username='joao',
        email='joao@teste.com',
        password=atribuir_hash(passwd_teste),
    )
    sessao_sql.add(usuario_cad_teste)
    sessao_sql.commit()
    sessao_sql.refresh(usuario_cad_teste)
    usuario_cad_teste.senha_limpa = passwd_teste
    return usuario_cad_teste
