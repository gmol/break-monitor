import random

from states import Config


class FakeSonar:

    counter = 0

    def get_distance(self):
        if Config.OVERTIME < self.counter < (Config.OVERTIME + Config.REST_TIME):
            return random.uniform(100.0, 250.0)
        if self.counter >= (Config.OVERTIME + Config.REST_TIME):
            self.counter = 0
        self.counter += 1
        return random.uniform(20.0, 99.0)
