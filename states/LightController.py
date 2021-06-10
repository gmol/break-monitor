import logging
from abc import ABC, abstractmethod

from states import SolidLight
from states.Constants import LightMode


class LightController(ABC):

    def __init__(self):
        self.light = SolidLight
        self.logger = logging.getLogger("LightController")

    def on(self, mode=LightMode.SOLID, config={}):
        self.logger.info(f"Light effect ${mode}, config ${config}")
        if mode == LightMode.SOLID:
            self.light = SolidLight
        self.light.on()
        pass

    # @abstractmethod
    def off(self):
        self.light.off()
        pass
