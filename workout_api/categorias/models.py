from sqlalchemy import Integer, String
from contrib.models import BaseModel
from sqlalchemy.orm import  Mapped, mapped_column, relationship

from workout_api.atleta.models import AtletaModel

class CategoriaModel(BaseModel):
    __tablename__= 'categorias'

    pk_id: Mapped[int]= mapped_column(Integer, primary_key = True)
    nome: Mapped[str]= mapped_column(String(50), unique= True, nullable=False)
    atleta: Mapped['AtletaModel']= relationship(back_populates='categorias')