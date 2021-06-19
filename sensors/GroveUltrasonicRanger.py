# import sys
import logging
import time
# import statistics
from grove.gpio import GPIO

_TIMEOUT1 = 1000
_TIMEOUT2 = 10000


def usleep(x): return time.sleep(x / 1000000.0)


class GroveUltrasonicRanger(object):
    def __init__(self, pin=16):
        self.logger = logging.getLogger("GroveUltrasonicRanger")
        self.dio = GPIO(pin)

    def _get_distance(self):
        self.dio.dir(GPIO.OUT)
        self.dio.write(0)
        usleep(2)
        self.dio.write(1)
        usleep(10)
        self.dio.write(0)

        self.dio.dir(GPIO.IN)

        t0 = time.time()
        count = 0
        while count < _TIMEOUT1:
            if self.dio.read():
                break
            count += 1
        if count >= _TIMEOUT1:
            return None

        t1 = time.time()
        count = 0
        while count < _TIMEOUT2:
            if not self.dio.read():
                break
            count += 1
        if count >= _TIMEOUT2:
            return None

        t2 = time.time()

        dt = int((t1 - t0) * 1000000)
        if dt > 530:
            return None

        distance = ((t2 - t1) * 1000000 / 29 / 2)  # cm

        return distance

    def get_distance(self):
        while True:
            start_time = time.time_ns()
            d = self._get_distance()
            if d and d < 500:
                # latency in milliseconds
                latency = round((time.time_ns() - start_time)/1e6)
                self.logger.debug("Distance measure latency [{}]".format(latency))
                return d
