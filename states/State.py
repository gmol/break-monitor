from abc import ABC, abstractmethod


class State(ABC):
    timer = 0

    def __init__(self, context):
        self.context = context

    @abstractmethod
    def evaluate(self, activity) -> None:
        pass

    def adjust_timer(self, offset):
        print(f"Timer [${self.timer}] adjusted to [${self.timer + offset}]")
        self.timer = max(0, self.timer + offset)
