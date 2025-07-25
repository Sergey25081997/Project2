from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class MovementType(Enum):
    income = "income"
    outcome = "outcome"


@dataclass
class BaseMovement:
    item_id: int
    created_at: datetime
    count: int
    type: MovementType


@dataclass
class Movement(BaseMovement):
    id: int

    @classmethod
    def from_tuple(cls, data: tuple[int, str, int, MovementType, int]) -> "Movement":
        item_id, created_at, count, type_, id_ = data
        return Movement(item_id, datetime.fromisoformat(created_at), count, type_, id_)


@dataclass
class BaseItem:
    title: str
    weight: int


@dataclass
class NullableBaseItem:
    id: int
    title: str | None
    weight: int | None


@dataclass
class Item(BaseItem):
    id: int
