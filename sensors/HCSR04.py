import logging
from sensors.Sonar import Sonar
from gpiozero import DistanceSensor
from states import Config


class HCSR04(Sonar):

    # Get the distance in cm
    def get_distance(self):
        distance = self.sensor.distance * 100
        self.logger.debug("Distance[{}]".format(distance))
        return distance

    def __init__(self):
        self.logger = logging.getLogger("HCSR04")
        trigger_pin = Config.hcsr04_config["trigger_pin"]
        echo_pin = Config.hcsr04_config["echo_pin"]
        self.logger.info("HCSR04 created with trigger_pin=[{}] and echo_pin=[{}]".format(trigger_pin, echo_pin))
        self.sensor = DistanceSensor(trigger=trigger_pin, echo=echo_pin, max_distance=2)
