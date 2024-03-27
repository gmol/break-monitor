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


class LightEffect(Enum):
    IDLE = 1
    REST = 2
    OVERTIME = 3
    ALERT = 4


class LightBrightness(Enum):
    MAX = 255
    MIN = 1


light_config = {
    LightEffect.IDLE: {
        "color": Color("green"),
        "brightness": 10
    },
    LightEffect.REST: {
        "color": Color("yellow"),
        "brightness": 50
    },
    LightEffect.OVERTIME: {
        "color": Color("red"),
        "brightness": 100
    },
    LightEffect.ALERT: {
        "color": Color("purple"),
        "brightness": LightBrightness.MAX.value,
        "blinking": True,
        "blinking_speed": 1.0  # blinks per second
    }
}
