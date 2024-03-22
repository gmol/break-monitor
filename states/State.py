import logging
from abc import ABC, abstractmethod


class State(ABC):
    restTimerStart = 0

    def __init__(self, context):
        self.context = context
        self.logger = logging.getLogger("State")
        self.name = None

    @abstractmethod
    def evaluate(self, activity) -> None:
        pass

    # TODO remove if not used
    # def adjust_timer(self, offset):
    #     self.logger.info(f"Timer [${round(self.restTimerStart)}] adjusted to [${round(self.restTimerStart + offset)}] by [${round(offset)}]")
    #     self.restTimerStart = max(0, self.restTimerStart + offset)
