import time

from detector.AverageDistance import AverageDistance
from typing import List

from detector.Sample import Sample


class WorkDetector:
    measurements = List[Sample]

    def __init__(self, context):
        pass

    def add_sample(self, sample: Sample):
        self.measurements.append(sample)
        pass

    def detect(self, strategy=AverageDistance()):
        if len(self.measurements) > 0:
            if len(self.measurements) > 1000:
                # TODO provide a better cleanup
                del self.measurements[0]
            current_time = time.time()
            return strategy.detect(self.measurements)
        return False

