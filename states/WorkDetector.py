from states.AverageDistance import AverageDistance
from typing import List

from states.Sample import Sample


class WorkDetector:
    measurements = List[Sample]

    def __init__(self, context):
        pass

    def add_sample(self, sample: Sample):
        self.measurements.append(sample)
        pass

    def detect(self, strategy=AverageDistance()):
        if len(self.measurements) > 0:
            return strategy.detect(self.measurements)
        return False

