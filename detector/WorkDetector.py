from detector.AverageDistance import AverageDistance
from typing import List

from detector.Sample import Sample
from light.LightController import LightController
from states.Constants import Activity
from states.Context import Context
from states.TimeProvider import TimeProvider


class WorkDetector:
    measurements = []

    def __init__(self, context: Context):
        self.context = context
        pass

    def add_sample(self, sample: Sample):
        self.measurements.append(sample)
        self.detect()
        self.clean_up()
        pass

    def detect(self, strategy=AverageDistance()):
        if len(self.measurements) > 0:
            work_detected = strategy.detect(self.measurements)
            if work_detected:
                self.context.update_action(Activity.WORKING)
            else:
                self.context.update_action(Activity.IDLE)
        return False

    def clean_up(self):
        if len(self.measurements) > 1000:
            # TODO provide a better cleanup
            del self.measurements[0]
