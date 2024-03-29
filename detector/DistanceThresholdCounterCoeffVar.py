import logging
import statistics
import time
from typing import List

from detector.DetectionStrategy import DetectionStrategy
from detector.DistanceThresholdCounter import DistanceThresholdCounter
from detector.Sample import Sample
from states import Config


class DistanceThresholdCounterCoefficientVar(DistanceThresholdCounter):
    OBSERVATION_WINDOW = Config.detection_strategy["DistanceThresholdCounter"]["observation_window"]
    DISTANCE_THRESHOLD = Config.detection_strategy["DistanceThresholdCounter"]["distance_threshold"]
    Samples = List[Sample]  # type hinting (typedef in C++)

    def __init__(self):
        self.logger = logging.getLogger("DistanceThresholdCounterCoefficientVar")
        self.logger.info("* observation_window[{}] distance_threshold[{}]"
                         .format(self.OBSERVATION_WINDOW, self.DISTANCE_THRESHOLD))

    def detect(self, measurements: Samples):
        super().detect(measurements)

    # def detect2(self, measurements: Samples):
    #     # TODO Use inherited method
    #     current_time_in_sec = round(time.time())
    #     recent_samples = list(filter(
    #         lambda s: s.timestamp >= current_time_in_sec - self.OBSERVATION_WINDOW, measurements
    #     ))
    #     # This will give initial time to display IP address and basically better estimation
    #     # if len(recent_samples) < 30:
    #     #     return False
    #
    #     # No new samples means a distance measure failure assume there is no user at the desk
    #     if len(recent_samples) < self.OBSERVATION_WINDOW / 4:
    #         self.logger.warning("Not enough measurements with the last observation window to estimate presence.")
    #         return False
    #
    #     cv = self.calculate_cv(recent_samples)
    #     if cv is not None:
    #         self.logger.info("Coefficient of Variation: {:.2f}".format(cv))
    #
    #     recent_distance_values = map(lambda s: s.distance, recent_samples)
    #     recent_distance_square_filter = map(lambda s: 1 if s < self.DISTANCE_THRESHOLD else 0, recent_distance_values)
    #     average_distance = statistics.mean(recent_distance_square_filter)
    #     self.logger.info(
    #         "Observed window[{}] Presence probability [{:.2f}]".format(len(recent_samples), average_distance))
    #     if average_distance >= 0.5:
    #         return True
    #     return False

    def calculate_cv(self, data):
        n = 30
        if len(data) < n:
            self.logger.info("Error: Data array should have at least {} samples.".format(n))
            return None
        else:
            last_n_samples = list(map(lambda s: s.distance, data[-n:]))
            # self.logger.info("Last n samples: {}".format(last_n_samples))
            # for s in last_n_samples:
            #     self.logger.info("Sample: {}".format(s))
            # last_n_samples = data[-n:]
            mean = statistics.mean(last_n_samples)
            std_dev = statistics.stdev(last_n_samples)  # Use ddof=1 to calculate unbiased estimate of standard deviation
            return (std_dev / mean) * 100

    def detect_still_signal(self, measurements):
        self.logger.info("DistanceThresholdCounterCoefficientVar: Detecting still signal")
        n = 30
        if len(measurements) < n:
            for s in measurements:
                self.logger.info("Sample: {}".format(s.distance))
            self.logger.info("Error: Data array should have at least {} samples.".format(n))
            return None
        else:
            last_n_samples = list(map(lambda s: s.distance, measurements[-n:]))
            mean = statistics.mean(last_n_samples)
            average_error = statistics.mean(list(map(lambda s: abs(s - mean), last_n_samples)))
            return (average_error / mean) * 100
