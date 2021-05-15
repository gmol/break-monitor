import time


# Class created for testing purpose to inject a mock
class TimeProvider:
    @staticmethod
    def get_current_time():
        return time.time()
