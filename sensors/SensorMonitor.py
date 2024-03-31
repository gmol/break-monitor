import logging
import time
from threading import Thread, Event

from detector.Sample import Sample
from detector.WorkDetector import WorkDetector
from sensors.Sonar import Sonar
from states import Config


class SensorMonitor:

    def __init__(self, work_detector: WorkDetector, sonar: Sonar):
        self._logger = logging.getLogger("SensorMonitor")
        self._work_detector = work_detector
        self._sonar = sonar

    # def start(self):
    #     self._schedule_repeatedly(1, self._collect_data)
    #     self.work_detector.start()

    def start_loop(self):
        while True:
            self._collect_data()
            self._work_detector.detect()
            # if Config.IS_DEBUG:
            #     self._logger.debug("Calling sleep(5)")
            #     time.sleep(5)
            # else:
            time.sleep(1)

    def _collect_data(self):
        distance = self._sonar.get_distance()
        if distance:
            timestamp = round(time.time())  # in seconds [int]
            self._work_detector.add_sample(Sample(timestamp, distance))

    # def _schedule_repeatedly(self, interval, func, *args):
    #     """
    #     Schedules a function to be called repeatedly with a specified interval.
    #
    #     :param interval: Time interval between function calls in seconds.
    #     :param func: Function to be called repeatedly.
    #     :param args: Arguments to be passed to the function.
    #     """
    #     # self.logger.info("* call_repeatedly interval [{}]".format(interval))
    #     stopped = Event()
    #
    #     def loop():
    #         while not stopped.wait(interval):  # the first call is in `interval` secs
    #             # self.logger.info(f"Thread's loop: ${func}")
    #             func(*args)
    #
    #     Thread(target=loop).start()
    #     return stopped.set
