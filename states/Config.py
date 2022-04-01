from enum import Enum
from colour import Color

REST_TIME = 5 * 60
OVERTIME = 45 * 60
OVERTIME_ALERT = 60 * 60

IS_DEBUG = False


class Activity(Enum):
    IDLE = 1
    WORKING = 2


class MqttConfig(Enum):
    TOPIC = "sensors/breakalert/state"
    HOST = "mqtt.eclipseprojects.io"
    USERNAME = "homeassistant"
    PASSWORD = "einge2aephoe7oachieth9Aegie1gohb0aepeewoon9cho8eid1ish3ailaecei2"


class LightColor(Enum):
    RED = Color("red")
    GREEN = Color("green")
    WHITE = Color("white")
    YELLOW = Color("yellow")
    BLUE = Color("blue")


class LightEffect(Enum):
    SOLID_RED = 1
    SOLID_GREEN = 2
    SOLID_YELLOW = 3
    SOLID_WHITE = 4
    SOLID_BLUE = 5
    BLINKING = 6
    SOLID_SELECTED_BLUE = 7
    SOLID_ARBITRARY = 8


class LightBrightness(Enum):
    MAX = 1.0
    MIN = 0.05


detection_strategy = {
    "AverageDistance": {
        "observation_window": 15,   # seconds
        "distance_threshold": 80,   # cm
    },
    "DistanceThresholdCounter": {
        "observation_window": 30,   # seconds
        "distance_threshold": 80,   # cm
    }
}

light_config = {
    LightEffect.SOLID_RED: {
        "color": LightColor.RED.value,
        "brightness": LightBrightness.MAX.value
    },
    LightEffect.SOLID_GREEN: {
        "color": LightColor.GREEN.value,
        "brightness": (LightBrightness.MAX.value / 2)
    },
    LightEffect.SOLID_YELLOW: {
        "color": LightColor.YELLOW.value,
        "brightness": LightBrightness.MIN.value
    },
    LightEffect.SOLID_BLUE: {
        "color": LightColor.BLUE.value,
        "brightness": LightBrightness.MIN.value
    },
    LightEffect.SOLID_WHITE: {
        "color": LightColor.WHITE.value,
        "brightness": LightBrightness.MIN.value
    },
    LightEffect.SOLID_ARBITRARY: {
        "brightness": LightBrightness.MIN.value,
        "LEDs": [
            LightColor.WHITE,
            None,
            LightColor.WHITE,
            None,
            LightColor.WHITE,
            None,
            LightColor.WHITE,
            None
        ],
        "ledConfig": [
            {"color": LightColor.WHITE, "brightness": LightBrightness.MIN.value},
            None,
            {"color": LightColor.WHITE, "brightness": LightBrightness.MIN.value},
            None,
            {"color": LightColor.WHITE, "brightness": LightBrightness.MIN.value},
            None,
            {"color": LightColor.WHITE, "brightness": LightBrightness.MIN.value},
            None
        ]
    },
    LightEffect.BLINKING: {
        "color": LightColor.RED.value,
        "brightness": LightBrightness.MAX.value,
        "blinking": True,
    }
}
