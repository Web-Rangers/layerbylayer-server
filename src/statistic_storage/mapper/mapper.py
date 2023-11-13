from typing import TypeVar, Type

from pydantic import BaseModel

from src.statistic_storage.abstract.const import Base

T = TypeVar('T')


class Mapper:
    @staticmethod
    def from_dto(dto, model_class: Type[T]) -> BaseModel:
        return model_class(**dto.dict())

    @staticmethod
    def to_dto(model, dto_class: Type[T]) -> Base:
        return dto_class(**model.__dict__)
