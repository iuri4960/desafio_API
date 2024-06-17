from typing import Annotated
from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseSchema


class CategoriaIn(BaseSchema):
     nome: Annotated[str, Field(description= 'nome da categoria', example='scale', max_length=10)]

class CategoriaOut(CategoriaIn):
     id: Annotated[UUID4, Field(description='identificador da categoria')]