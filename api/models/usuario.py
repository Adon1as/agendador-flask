from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from api.service import db
import json


class Usuario(db.Model):
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    nome: Mapped[str] = mapped_column(String(128),nullable=False)
    cpf: Mapped[str] = mapped_column(String(14),unique=True)
    
        
    def as_dict(self):
        data = {}
        for atribute in self.__table__.columns:
            data[atribute.name] = getattr(self, atribute.name)
        return data