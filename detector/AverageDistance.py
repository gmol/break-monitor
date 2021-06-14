import logging
import statistics
import time
from typing import List

from detector.DetectionStrategy import DetectionStrategy
from detector.Sample import Sample


class AverageDistance(DetectionStrategy):

    OBSERVATION_WINDOW = 15  # seconds
    DISTANCE_THRESHOLD = 100
    Samples = List[Sample]

    def __init__(self):
        self.logger = logging.getLogger("AverageDistance")

    def detect(self, measurements: Samples):
        current_time_in_sec = round(time.time())
        recent_samples = list(filter(
            lambda s: s.timestamp >= current_time_in_sec - self.OBSERVATION_WINDOW, measurements
        ))
        recent_distance_values = map(lambda s: s.distance, recent_samples)
        average_distance = statistics.mean(recent_distance_values)
        self.logger.info("Obseved window[{}] Average distance[{}]".format(len(recent_samples), average_distance))
        if average_distance < self.DISTANCE_THRESHOLD:
            return True
        return False
