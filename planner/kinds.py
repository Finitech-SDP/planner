from typing import Any, Dict
import enum


class Tile:
    @enum.unique
    class TileType(enum.IntEnum):
        BLOCKED = enum.auto()
        HUB = enum.auto()
        PARKING = enum.auto()
        ROAD = enum.auto()

    def __init__(self, x: int, y: int, type_: "Tile.TileType"):
        self.x = x
        self.y = y
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
        return cls(dict_["x"], dict_["y"], type_map[dict_["type"]])


class Car:
    @enum.unique
    class CarStatus(enum.IntEnum):
        NOTHING = enum.auto()
        AWAITING_DELIVERY = enum.auto()
        AWAITING_PARKING = enum.auto()

    def __init__(self, x: int, y: int, status: "Car.CarStatus"):
        self.x = x
        self.y = y
        self.status = status


class Robot:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
