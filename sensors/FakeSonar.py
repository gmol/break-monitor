from random import random


class FakeSonar:

    @staticmethod
    def get_distance():
        return random.uniform(20.0, 99.0)
