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
        self.color = config["color"]
        self.logger.info("Color [{}]".format(self.color))
        self.brightness = 1.0
        if "brightness" in config:
            self.brightness = config["brightness"]
        self.logger.info("Brightness [{}]".format(self.brightness))

    def on(self):
        self.logger.info("Solid Light ON color=[{}]".format(self.color))
        blinkt.clear()
        # for i in range(7):
        #     blinkt.set_pixel(i + 1, self.r, self.g, self.b, self.brightness)
        # blinkt.set_all(self.r, self.g, self.b, self.brightness)
        # rgb = self.color.rgb
        rgb = [int(x * 255) for x in self.color.rgb]
        blinkt.set_all(rgb[0], rgb[1], rgb[2], self.brightness)
        blinkt.show()
        pass

    def off(self):
        self.logger.info("Solid Light OFF")
        blinkt.clear()
        blinkt.show()
        pass
