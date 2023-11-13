from typing import TypeVar, Type

T = TypeVar('T')


class Mapper:
    @staticmethod
    def from_dto(dto, model_class: Type[T]) -> T:
        return model_class(**dto.dict())

    @staticmethod
    def to_dto(model, dto_class: Type[T]) -> T:
        return dto_class(**model.__dict__)
