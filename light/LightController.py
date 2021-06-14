import logging
from abc import ABC

# from states import SolidLight
from states.Config import LightEffect
from states.Config import LightColor
from pprint import pprint

from light.SolidLight import SolidLight


class LightController(ABC):

    def __init__(self):
        self.logger = logging.getLogger("LightController")
        self.logger.info("LightController created")
        self.light = None
        self.currentEffect = None

    def on(self, effect=LightEffect.SOLID_RED):
        # self.logger.info(f"Light effect ${effect}, config ${config}")
        if self.currentEffect != effect:
            self.currentEffect = effect
            if effect == LightEffect.SOLID_GREEN:
                self.light = SolidLight({
                    "color": LightColor.GREEN,
                    "brightness": 0.05
                })
            elif effect == LightEffect.SOLID_YELLOW:
                self.light = SolidLight({
                    "color": LightColor.YELLOW,
                    "brightness": 0.05
                })
            elif effect == LightEffect.SOLID_WHITE:
                self.light = SolidLight({"color": LightColor.WHITE})
            elif effect == LightEffect.SOLID_BLUE:
                self.light = SolidLight({"color": LightColor.BLUE})
            else:
                self.light = SolidLight({"color": LightColor.RED})
            self.light.on()
        pass

    # @abstractmethod
    def off(self):
        if self.light:
            self.light.off()
        self.light = None
        pass
