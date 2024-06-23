from typing import Annotated
from pydantic import Field, PositiveFloat
from project.contrib.schemas import BaseSchema


class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Atleta', example='Pedro', max_length=50)]
    cpf: Annotated[str, Field(description='Cpf do Atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do Atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', example=75.5)]
    altura: Annotated[int, Field(description='Altura do Atleta', example=1.70)]
    sexo: Annotated[str, Field(description='Sexo do Atleta', example='M', max_length=1)]
