from abc import ABC, abstractmethod


class Light(ABC):

    @abstractmethod
    def on(self, config={}):
        pass

    @abstractmethod
    def off(self):
        pass
