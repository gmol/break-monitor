from enum import Enum

REST_TIME = 45
OVERTIME = 1 * 60

IS_DEBUG = False

class Activity(Enum):
    IDLE = 1
    WORKING = 2


class LightColor(Enum):
    RED = 1
    GREEN = 2
    WHITE = 3
    YELLOW = 4
    BLUE = 5


class LightEffect(Enum):
    SOLID_RED = 1
    SOLID_GREEN = 2
    SOLID_YELLOW = 3
    SOLID_WHITE = 4
    SOLID_BLUE = 5
    BLINKING = 6
