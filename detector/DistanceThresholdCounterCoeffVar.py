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
        return super().detect(measurements)

    # def calculate_cv(self, data):
    #     n = 30
    #     if len(data) < n:
    #         self.logger.info("Error: Data array should have at least {} samples.".format(n))
    #         return None
    #     else:
    #         last_n_samples = list(map(lambda s: s.distance, data[-n:]))
    #         # self.logger.info("Last n samples: {}".format(last_n_samples))
    #         # for s in last_n_samples:
    #         #     self.logger.info("Sample: {}".format(s))
    #         # last_n_samples = data[-n:]
    #         mean = statistics.mean(last_n_samples)
    #         std_dev = statistics.stdev(last_n_samples)
    #         return (std_dev / mean) * 100

    def detect_no_movement(self, measurements):
        if Config.IS_DEBUG:
            n = int(self.OBSERVATION_WINDOW / 3)
        else:
            n = int(self.OBSERVATION_WINDOW)
        if len(measurements) < n:
            self.logger.info("No movement detection: not enough data")
            return None
        else:
            last_n_samples = list(map(lambda s: s.distance, measurements[-n:]))
            mean = statistics.mean(last_n_samples)
            average_error = statistics.mean(list(map(lambda s: abs(s - mean), last_n_samples)))
            self.logger("No movement detection result: {}".format(((average_error / mean) * 100)))
            return ((average_error / mean) * 100) < 2
