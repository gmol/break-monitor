import logging
from abc import ABC

from light.BlinkingLight import BlinkingLight
from light.SolidLight import SolidLight
from states import Config


class LightController(ABC):

    def __init__(self):
        self.logger = logging.getLogger("LightController")
        self.logger.info("LightController created")
        self.light = None
        self.currentEffect = None

    def light_on(self, effect):
        if "color" not in effect:
            raise ValueError("'color' is required for light config")
        if "brightness" not in effect:
            raise ValueError("'brightness' is required for light config")
        if self.currentEffect != effect:
            self.currentEffect = effect
            light_config = Config.light_config[self.currentEffect]
            self.logger.info("Light Config[{}]".format(light_config))
            if self.currentEffect == Config.LightEffect.BLINKING:
                self.light = BlinkingLight(light_config)
            else:
                self.light = SolidLight(light_config)
            self.light.on()

    def light_off(self):
        if self.light:
            self.logger.info("Light OFF")
            self.light.light_off()
        self.light = None
