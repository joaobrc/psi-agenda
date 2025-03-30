from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from jwt import encode
from pwdlib import PasswordHash

from .settings import Settings

PWD_CONTEXT = PasswordHash.recommended()
SECRET_KEY = Settings().SECRET_KEY
ACCESS_EXP = Settings().ACCESS_TOKEN_EXPIRE_MINUTES
ALGORITIMO = Settings().ALGORITOMO


def criar_acesso_token(dados: dict):
    dados_para_encode = dados.copy()
    expiracao_token = datetime.now(tz=ZoneInfo('UTC')) + timedelta(
        minutes=ACCESS_EXP
    )
    dados_para_encode.update({'exp': expiracao_token})
    token_encodado = encode(
        dados_para_encode, key=SECRET_KEY, algorithm=ALGORITIMO
    )
    return token_encodado


def atribuir_hash(senha: str) -> str:
    return PWD_CONTEXT.hash(senha)


def verificar_senha(senha: str, hash: str) -> bool:
    return PWD_CONTEXT.verify(senha, hash)
