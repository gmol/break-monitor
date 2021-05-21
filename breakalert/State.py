from abc import ABC, abstractmethod


class State(ABC):

    def __init__(self, context):
        self.context = context

    @abstractmethod
    def evaluate(self, activity) -> None:
        pass
