import logging
from abc import ABC

# from states import SolidLight
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

    def on(self, effect=LightEffect.SOLID_RED):
        # self.logger.info(f"Light effect ${effect}, config ${config}")
        if self.currentEffect != effect:
            self.currentEffect = effect
            light_config = Config.light_config[self.currentEffect]
            self.logger.info("Light Config[{}]".format(light_config))
            self.logger.info("Light Config color[{}]".format(light_config["color"]))
            self.logger.info("Light Config brightness [{}]".format(light_config["brightness"]))
            # if effect == LightEffect.SOLID_GREEN:
            self.light = SolidLight(light_config)
            # elif effect == LightEffect.SOLID_YELLOW:
            #     self.light = SolidLight(Config.light_config[LightEffect.SOLID_YELLOW])
            # elif effect == LightEffect.SOLID_WHITE:
            #     self.light = SolidLight(Config.light_config[LightEffect.SOLID_WHITE])
            # elif effect == LightEffect.SOLID_BLUE:
            #     self.light = SolidLight(Config.light_config[LightEffect.SOLID_BLUE])
            # else:
            #     self.light = SolidLight(Config.light_config[LightEffect.SOLID_RED])
            self.light.on()
        pass

    # @abstractmethod
    def off(self):
        if self.light:
            self.light.off()
        self.light = None
        pass
