import logging
from abc import ABC

# from states import SolidLight
from light.BlinkingLight import BlinkingLight
from states import Config
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

    def on(self, effect=LightEffect.SOLID_RED, extra_config=None):
        if self.currentEffect != effect:
            self.currentEffect = effect
            # SOLID_ARBITRARY is dynamically created that is why it need an extra config
            if self.currentEffect == Config.LightEffect.SOLID_ARBITRARY and extra_config:
                light_config = extra_config
            else:
                light_config = Config.light_config[self.currentEffect]
            self.logger.info("Light Config[{}]".format(light_config))
            if self.currentEffect == Config.LightEffect.BLINKING:
                self.light = BlinkingLight(light_config)
            else:
                self.light = SolidLight(light_config)
            self.light.on()

    def off(self):
        if self.light:
            self.logger.info("Light OFF")
            self.light.off()
        self.light = None
