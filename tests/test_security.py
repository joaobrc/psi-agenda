from jwt import decode

from src.psi_agenda.security import (
    atribuir_hash,
    criar_acesso_token,
    verificar_senha,
)
from src.psi_agenda.settings import Settings


def test_criar_acesso_token():
    secret_key = Settings().SECRET_KEY
    algoritmo = Settings().ALGORITOMO
    dados = {'email': 'joao@teste.com'}
    dados_encode = criar_acesso_token(dados=dados)
    dados_decode = decode(dados_encode, key=secret_key, algorithms=algoritmo)
    assert type(dados_decode) is dict
    assert dados_decode['email'] == dados['email']
    assert 'exp' in dados_decode


def test_verificar_senha():
    senha = '123'
    senha_em_hash = atribuir_hash(senha=senha)
    verficar = verificar_senha(senha=senha, hash=senha_em_hash)
    status = True
    assert verficar == status
