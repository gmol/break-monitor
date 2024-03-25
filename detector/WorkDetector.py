import logging
from threading import Event, Thread

from detector import DetectionStrategy
from detector.DistanceThresholdCounter import DistanceThresholdCounter
from detector.Sample import Sample
from states import Config

from states.Config import Activity
from states.Context import Context


class WorkDetector:

    def __init__(self, context: Context, detection_strategy: DetectionStrategy):
        self._measurements = []
        self._logger = logging.getLogger("WorkDetector")
        self._context = context
        self._detectionStrategy = detection_strategy

    def add_sample(self, sample: Sample):
        self._measurements.append(sample)
        # self.detect()
        self.clean_up()

    # def start(self):
    #     # TODO Strategy is not configurable
    #     if Config.IS_DEBUG:
    #         self.call_repeatedly(5, self.detect, DistanceThresholdCounter())
    #     else:
    #         self.call_repeatedly(1, self.detect, DistanceThresholdCounter())

    # def detect(self, strategy):
    #     self._logger.info("* detect")
    #     if len(self._measurements) > 0:
    #         work_detected = strategy.detect(self._measurements)
    #         if work_detected:
    #             self._context.update_action(Activity.WORKING)
    #         else:
    #             self._context.update_action(Activity.IDLE)

    def detect(self):
        self._logger.info("* detect")
        if len(self._measurements) > 0:
            work_detected = self._detectionStrategy.detect(self._measurements)
            if work_detected:
                self._context.update_action(Activity.WORKING)
            else:
                self._context.update_action(Activity.IDLE)

    def clean_up(self):
        if len(self._measurements) > 1000:
            # TODO provide a better cleanup
            del self._measurements[0]

    # def call_repeatedly(self, interval, func, *args):
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
