from enum import Enum

REST_TIME = 5
OVERTIME = 3


class Activity(Enum):
    IDLE = 1
    WORKING = 2


class LightColor(Enum):
    RED = 1
    GREEN = 2
    WHITE = 3


class LightMode(Enum):
    SOLID = 1
    BLINKING = 2
