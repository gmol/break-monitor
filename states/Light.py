from abc import ABC, abstractmethod

from states.Constants import LightMode


class Light(ABC):
    # @abstractmethod
    def on(self, mode=LightMode.SOLID, config={}):
        pass

    # @abstractmethod
    def off(self):
        pass
