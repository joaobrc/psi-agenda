from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registro = registry()


@table_registro.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    update_at: Mapped[datetime] = mapped_column(
        init=False, onupdate=func.now(), default=func.now()
    )


@table_registro.mapped_as_dataclass
class Profissional:
    __tablename__ = 'profissionais'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]
    data_admissao: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    data_desligamento: Mapped[datetime | None] = mapped_column(nullable=True)
    numero_conselho: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    upadate_at: Mapped[datetime] = mapped_column(
        init=False, onupdate=func.now(), default=func.now()
    )
