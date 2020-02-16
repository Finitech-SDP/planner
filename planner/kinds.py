import enum


class Tile:
    @enum.unique
    class TileType(enum.IntEnum):
        ROAD = enum.auto()

    def __init__(self, x: int, y: int, type_: "Tile.TileType"):
        self.x = x
        self.y = y
        self.type = type_


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
