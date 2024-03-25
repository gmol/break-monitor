import os
import sys
from enum import Enum

if 'darwin' in sys.platform:
    import tests.board as board  # for mac
else:
    import board

from colour import Color

REST_TIME = 5 * 60
OVERTIME = 45 * 60
OVERTIME_ALERT = 60 * 60

IS_DEBUG = False

pixel_pin = board.D12
num_pixels = 1


class Activity(Enum):
    IDLE = 1
    WORKING = 2


class MqttConfig:
    TOPIC = "sensors/breakalert/state"
    PASSWORD = os.environ.get('MQTT_PASSWORD', None)
    HOST = os.environ.get('MQTT_HOST', None)
    USERNAME = "homeassistant"


hcsr04_config = {
    "trigger_pin": 23,
    "echo_pin": 24
}

detection_strategy = {
    "AverageDistance": {
        "observation_window": 15,  # seconds
        "distance_threshold": 80,  # cm
    },
    "DistanceThresholdCounter": {
        "observation_window": 30,  # seconds
        "distance_threshold": 80,  # cm
    }
}


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
    MAX = 255
    MIN = 1


light_config = {
    LightEffect.SOLID_RED: {
        "color": LightColor.RED.value,
        "brightness": 100
    },
    LightEffect.SOLID_GREEN: {
        "color": LightColor.GREEN.value,
        "brightness": 50
    },
    LightEffect.SOLID_YELLOW: {
        "color": LightColor.YELLOW.value,
        "brightness": LightBrightness.MIN.value
    },
    LightEffect.SOLID_BLUE: {
        "color": LightColor.BLUE.value,
        "brightness": 10
    },
    LightEffect.SOLID_WHITE: {
        "color": LightColor.WHITE.value,
        "brightness": LightBrightness.MIN.value
    },
    LightEffect.BLINKING: {
        "color": LightColor.RED.value,
        "brightness": LightBrightness.MAX.value,
        "blinking": True,
        "blinking_speed": 1.0  # blinks per second
    }
}
