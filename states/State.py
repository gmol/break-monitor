import logging
from abc import ABC, abstractmethod


class State(ABC):
    timer = 0

    def __init__(self, context):
        self.context = context
        self.logger = logging.getLogger("State")

    @abstractmethod
    def evaluate(self, activity) -> None:
        pass

    def adjust_timer(self, offset):
        self.logger.info(f"Timer [${round(self.timer)}] adjusted to [${round(self.timer + offset)}] by [${round(offset)}]")
        self.timer = max(0, self.timer + offset)
