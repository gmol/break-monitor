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
        self.currentLightConfig = None

    def light_on(self, light_config):
        if "color" not in light_config:
            raise ValueError("'color' is required for light config")
        if "brightness" not in light_config:
            raise ValueError("'brightness' is required for light config")
        if self.currentLightConfig != light_config:
            self.currentLightConfig = light_config
            # light_config = Config.light_config[self.currentEffect]
            self.logger.info("Light Config[{}]".format(light_config))
            if self.currentLightConfig == Config.LightEffect.BLINKING:
                self.light = BlinkingLight(light_config)
            else:
                self.light = SolidLight(light_config)
            self.light.on()

    def light_off(self):
        if self.light:
            self.logger.info("Light OFF")
            self.light.light_off()
        self.light = None
