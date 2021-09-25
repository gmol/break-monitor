import logging

from detector.DistanceThresholdCounter import DistanceThresholdCounter
from detector.Sample import Sample

from states.Config import Activity
from states.Context import Context



class WorkDetector:
    measurements = []

    def __init__(self, context: Context):
        self.logger = logging.getLogger("WorkDetector")
        self.context = context
        pass

    def add_sample(self, sample: Sample):
        self.measurements.append(sample)
        self.detect()
        self.clean_up()
        pass

    def detect(self, strategy=DistanceThresholdCounter()):
        if len(self.measurements) > 0:
            work_detected = strategy.detect(self.measurements)
            if work_detected:
                self.context.update_action(Activity.WORKING)
            else:
                self.context.update_action(Activity.IDLE)
        pass

    def clean_up(self):
        if len(self.measurements) > 1000:
            # TODO provide a better cleanup
            del self.measurements[0]

