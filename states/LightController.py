import logging
from abc import ABC, abstractmethod

# from states import SolidLight
from states.Constants import LightMode
from pprint import pprint

from states.SolidLight import SolidLight


class LightController(ABC):

    def __init__(self):
        self.logger = logging.getLogger("LightController")
        self.logger.info("LightController created")
        self.light = SolidLight()

    def on(self, mode=LightMode.SOLID, config={}):
        self.logger.info(f"Light effect ${mode}, config ${config}")
        if mode == LightMode.SOLID:
            self.light = SolidLight()
        self.logger.info(self.light)
        pprint(vars(self.light))
        self.light.on()
        pass

    # @abstractmethod
    def off(self):
        self.logger.info("LightController light OFF")
        self.light.off()
        pass
