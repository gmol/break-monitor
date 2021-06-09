import time

from states.Sample import Sample


class SensorMonitor:

    def __init__(self, work_detector, ranger):
        self.work_detector = work_detector
        self.ranger = ranger
        pass

    def monitor(self):
        while True:
            distance = self.ranger.get_distance()
            if distance < 500:
                timestamp = round(time.time())  # in seconds
                sample = Sample(timestamp, distance)
                self.work_detector.add_sample(sample)
            time.sleep(1)


