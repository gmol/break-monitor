import logging
import random

from sensors.Sonar import Sonar
from states import Config


class FakeSonar(Sonar):

    counter = 0

    def __init__(self):
        self.logger = logging.getLogger("FakeSonar")

    def get_distance(self):
        self.logger.info("Counter [{}]".format(self.counter))
        if self.counter < 5:
            self.logger.info("Initial rand distance 100-250cm")
            return random.uniform(100.0, 250.0)
        if Config.OVERTIME < self.counter < (Config.OVERTIME + Config.REST_TIME):
            self.logger.info("Rand distance 100-250cm")
            return random.uniform(100.0, 250.0)
        if self.counter >= (Config.OVERTIME + Config.REST_TIME):
            self.logger.info("Reset counter")
            self.counter = 0
        self.counter += 1
        self.logger.info("Rand distance 20-99cm")
        return random.uniform(20.0, 99.0)
