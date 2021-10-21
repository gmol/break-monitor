import logging
import statistics
import time
from typing import List

from detector.DetectionStrategy import DetectionStrategy
from detector.Sample import Sample
from states import Config


class DistanceThresholdCounter(DetectionStrategy):
    OBSERVATION_WINDOW = Config.detection_strategy["DistanceThresholdCounter"]["observation_window"]
    DISTANCE_THRESHOLD = Config.detection_strategy["DistanceThresholdCounter"]["distance_threshold"]
    Samples = List[Sample]

    def __init__(self):
        self.logger = logging.getLogger("DistanceThresholdCounter")
        self.logger.info("* DistanceThresholdCounter observation_window[{}] distance_threshold[{}]"
                         .format(self.OBSERVATION_WINDOW, self.DISTANCE_THRESHOLD))

    def detect(self, measurements: Samples):
        current_time_in_sec = round(time.time())
        recent_samples = list(filter(
            lambda s: s.timestamp >= current_time_in_sec - self.OBSERVATION_WINDOW, measurements
        ))
        # This will give initial time to display IP address and basically better estimation
        # if len(recent_samples) < 30:
        #     return False

        # No new samples means a distance measure failure assume there is no user at the desk
        if len(recent_samples) < self.OBSERVATION_WINDOW / 4:
            self.logger.warning("Distance measure failure assume there is no user at the desk")
            return False

        recent_distance_values = map(lambda s: s.distance, recent_samples)
        recent_distance_square_filter = map(lambda s: 1 if s < self.DISTANCE_THRESHOLD else 0, recent_distance_values)
        average_distance = statistics.mean(recent_distance_square_filter)
        self.logger.info(
            "Observed window[{}] Presence probability [{:.2f}]".format(len(recent_samples), average_distance))
        if average_distance >= 0.5:
            return True
        return False
