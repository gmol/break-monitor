import time


# Class created for testing purpose to inject a mock
class TimeProvider:

    # Returns the time as a floating point number expressed in seconds since the epoch, in UTC
    @staticmethod
    def get_current_time():
        return time.time()
