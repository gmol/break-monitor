from abc import ABC, abstractmethod

from Constants import LightMode, LightColor


class Light(ABC):
    # @abstractmethod
    def on(self, color=LightColor.RED, mode=LightMode.SOLID):
        pass

    # @abstractmethod
    def off(self, color=LightColor.RED):
        pass
