import sys
import logging

import colour
if 'darwin' in sys.platform:
    import tests.neopixel as neopixel
else:
    import neopixel

from light.Light import Light
from states.Config import pixel_pin, num_pixels


# if 'win32' in sys.platform:
#     import light.FakeBlinkt as blinkt
# if 'darwin' in sys.platform:
#     import light.FakeBlinkt as blinkt
# else:
#     import blinkt


class SolidLight(Light):

    def __init__(self, config: dict = {}):
        self.logger = logging.getLogger("SolidLight")
        self.logger.info("Solid Light created{}".format(config))
        if "color" not in config:
            raise ValueError("Color is required for SolidLight")
        if "brightness" not in config:
            raise ValueError("Brightness is required for SolidLight")
        self.color: colour.Color = config["color"]
        self.brightness: float = config["brightness"]
        self.pixels = neopixel.NeoPixel(
            pixel_pin, num_pixels, pixel_order=neopixel.RGB, brightness=self.brightness
        )

    def on(self):
        self.logger.info("Solid Light ON color=[{}]".format(self.color))
        color255 = self.multiply_tuple((self.color.get_red(), self.color.get_green(), self.color.get_blue()), 255)
        self.pixels.fill(color255)
        self.pixels.show()

    @staticmethod
    def multiply_tuple(tuple_object, scalar):
        return tuple(scalar * elem for elem in tuple_object)

    def off(self):
        self.logger.info("Solid Light OFF")
        self.pixels.fill(0)
        self.pixels.show()
