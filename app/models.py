from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship, Mapped
from typing import List
from . import db 


class Usuario(db.Model):
    __tablename__ = 'usuario'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
    email = mapped_column(db.String(64), nullable=False)
    senha = mapped_column(db.String(128), nullable=False)
    personagens: Mapped[List["Personagem"]] = relationship(back_populates="dono")


class Personagem(db.Model):
    __tablename__ = 'personagem'

    id: Mapped[int] = mapped_column(primary_key=True)
    dono_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)
    nome: Mapped[String] = mapped_column(db.String(32), nullable=False)
    vida: Mapped[int] = mapped_column(db.Integer, default=20, nullable=False)

    dono: Mapped["Usuario"] = relationship(back_populates="personagens")
