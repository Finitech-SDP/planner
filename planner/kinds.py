from typing import Any, Dict
import enum


class Tile:
    @enum.unique
    class TileType(enum.IntEnum):
        BLOCKED = enum.auto()
        HUB = enum.auto()
        PARKING = enum.auto()
        ROAD = enum.auto()

    def __init__(self, row: int, column: int, type_: "Tile.TileType"):
        self.row = row
        self.column = column
        self.type = type_
        self.is_temporarily_blocked = False

    @classmethod
    def from_dict(cls, dict_: Dict[str, Any]) -> "Tile":
        type_map = {
            "blocked": cls.TileType.BLOCKED,
            "hub": cls.TileType.HUB,
            "parking": cls.TileType.PARKING,
            "road": cls.TileType.ROAD
        }
        return cls(dict_["row"], dict_["column"], type_map[dict_["type"]])


class Car:
    @enum.unique
    class CarStatus(enum.IntEnum):
        NOTHING = enum.auto()
        AWAITING_DELIVERY = enum.auto()
        AWAITING_PARKING = enum.auto()

    def __init__(self, row: int, column: int, status: "Car.CarStatus"):
        self.row = row
        self.column = column
        self.status = status


class Robot:
    def __init__(self, row: float, column: float):
        self.row = row
        self.column = column
