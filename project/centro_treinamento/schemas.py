from typing import Annotated
from pydantic import Field
from project.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro Treinamento', example='CT King', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do Centro Treinamento', example='Rua X, QD 02', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário d Centro Treinamento', example='Pedro', max_length=30)]