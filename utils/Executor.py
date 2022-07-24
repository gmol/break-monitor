import logging
from threading import Event, Thread


class Executor:
    def __init__(self):
        self.logger = logging.getLogger("Executor")

    def call_repeatedly(self, interval, func, *args):
        # self.logger.info("* call_repeatedly interval [{}]".format(interval))
        stopped = Event()

        def loop():
            while not stopped.wait(interval):  # the first call is in `interval` secs
                # self.logger.info(f"Thread's loop: ${func}")
                try:
                    func(*args)
                except Exception as ex:
                    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                    message = template.format(type(ex).__name__, ex.args)
                    self.logger.error(message)
                    self.logger.exception(ex)

        Thread(target=loop).start()
        return stopped.set
