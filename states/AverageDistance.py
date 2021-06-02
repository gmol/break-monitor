import statistics
import time
from typing import List

from states.DetectionStrategy import DetectionStrategy
from states.Sample import Sample


class AverageDistance(DetectionStrategy):

    OBSERVATION_WINDOW = 15  # seconds
    DISTANCE_THRESHOLD = 100
    Samples = List[Sample]

    def detect(self, measurements: Samples):
        current_time_in_sec = round(time.time())
        recent_samples = list(filter(
            lambda s: s.timestamp >= current_time_in_sec - self.OBSERVATION_WINDOW, measurements
        ))
        recent_distance_values = map(lambda s: s.distance, recent_samples)
        average_distance = statistics.mean(recent_distance_values)
        if average_distance < self.DISTANCE_THRESHOLD:
            return True
        return False
