from typing import Annotated
from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description= 'nome do centro de treinamento', example='CT', max_length=20)]
    endereco: Annotated[str, Field(description= 'endereço do centro de treinamento', example='Rua x, Q02', max_length=60)]
    proprietario: Annotated[str, Field(description= 'proprietario do centro de treinamento', example='Marcos', max_length=30)]

class CentroTreinamentoAtleta(BaseSchema):
     nome: Annotated[str, Field(description= 'nome do centro de treinamento', example='CT', max_length=20)]

class CentroTreinamentoOut(CentroTreinamentoIn):
     id: Annotated[UUID4, Field(description='identificador do centro de treinamento')]