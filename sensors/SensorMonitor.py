import logging
import time
from threading import Thread, Event

from detector.Sample import Sample
from detector.WorkDetector import WorkDetector
from sensors.Sonar import Sonar
from states import Config


class SensorMonitor:

    def __init__(self, work_detector: WorkDetector, sonar: Sonar):
        self.logger = logging.getLogger("SensorMonitor")
        self.work_detector = work_detector
        self.sonar = sonar

    def start(self):
        self.schedule_repeatedly(1, self.monitor)
        self.work_detector.start()

    def monitor(self):
        # while True:
        distance = self.sonar.get_distance()
        # self.logger.info("Distance[{}]".format(round(distance)))  # TODO REMOVE
        if distance:
            timestamp = round(time.time())  # in seconds [int]
            sample = Sample(timestamp, distance)
            self.work_detector.add_sample(sample)
        if Config.IS_DEBUG:
            time.sleep(5)
        else:
            time.sleep(1)

    def schedule_repeatedly(self, interval, func, *args):
        """
        Schedules a function to be called repeatedly with a specified interval.

        :param interval: Time interval between function calls in seconds.
        :param func: Function to be called repeatedly.
        :param args: Arguments to be passed to the function.
        """
        # self.logger.info("* call_repeatedly interval [{}]".format(interval))
        stopped = Event()

        def loop():
            while not stopped.wait(interval):  # the first call is in `interval` secs
                # self.logger.info(f"Thread's loop: ${func}")
                func(*args)

        Thread(target=loop).start()
        return stopped.set
