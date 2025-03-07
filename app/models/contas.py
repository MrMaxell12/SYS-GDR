from sqlalchemy.orm import mapped_column
from .. import db 

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = mapped_column(db.Integer, primary_key=True)
    username = mapped_column(db.String(32), unique=True, index=True)
    email = mapped_column(db.String(64))
    senha = mapped_column(db.String(128))


