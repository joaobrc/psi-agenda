from sqlalchemy import select

from src.psi_agenda.database import DATABASE_URI
from src.psi_agenda.models import Profissional, User


def test_database_uri():
    caminho = 'sqlite:///database.db'
    assert DATABASE_URI == caminho


def test_criar_usuario_no_banco(sessao_sql):
    usuario = User(username='joao', email='joao@teste.com', password='Sena')
    sessao_sql.add(usuario)
    sessao_sql.commit()
    user_db = sessao_sql.scalar(select(User).where(User.username == 'joao'))

    assert user_db.username == 'joao'


def test_criar_profisssonal_no_banco(sessao_sql):
    profi = Profissional(
        nome='Joao', numero_conselho='2353', data_desligamento=None
    )
    sessao_sql.add(profi)
    sessao_sql.commit()
    profi_db = sessao_sql.scalar(
        select(Profissional).where(Profissional.nome == 'Joao')
    )
    assert profi_db.nome == 'Joao'
