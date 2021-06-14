import logging
import sys

from states import Config

if 'win32' in sys.platform:
    import light.FakeBlinkt as blinkt
else:
    import blinkt

from light.Light import Light


class SolidLight(Light):

    def __init__(self, config={"color": Config.LightColor.RED}):
        self.logger = logging.getLogger("SolidLight")
        self.logger.info("Solid Light created{}".format(config))
        self.r = 255
        self.g = self.b = 0
        if config["color"] == Config.LightColor.GREEN:
            self.r = self.b = 0
            self.g = 255
        if config["color"] == Config.LightColor.YELLOW:
            self.r = self.g = 255
            self.b = 0
        if config["color"] == Config.LightColor.WHITE:
            self.r = self.g = self.b = 0
        if config["color"] == Config.LightColor.BLUE:
            self.r = self.g = 0
            self.b = 255

        self.brightness = 1.0
        if "brightness" in config:
            self.brightness = config["brightness"]
        self.logger.info("Brightness [{}]".format(self.brightness))

    def on(self):
        self.logger.info("Solid Light ON r={} g={} b={}".format(self.r, self.g, self.b))
        blinkt.clear()
        blinkt.set_all(self.r, self.g, self.b, self.brightness)
        blinkt.show()
        pass

    def off(self):
        self.logger.info("Solid Light OFF")
        blinkt.clear()
        blinkt.show()
        pass
