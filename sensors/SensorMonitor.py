import logging
import time

from detector.Sample import Sample
from detector.WorkDetector import WorkDetector
from sensors.FakeSonar import FakeSonar


class SensorMonitor:

    def __init__(self, work_detector, ranger):
        self.logger = logging.getLogger("SensorMonitor")
        self.work_detector = work_detector
        self.ranger = ranger
        pass

    def monitor(self):
        while True:
            distance = self.ranger.get_distance()
            self.logger.info("Distance[{}]".format(distance))
            if distance:
                timestamp = round(time.time())  # in seconds [int]
                sample = Sample(timestamp, distance)
                self.work_detector.add_sample(sample)
            time.sleep(1)
