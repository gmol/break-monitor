import logging

import blinkt
from states.Light import Light


class SolidLight(Light):

    def __init__(self):
        self.logger = logging.getLogger("SolidLight")
        self.logger.info("Solid Light created")

    def on(self, config={}):
        self.logger.info("Solid Light ON")
        r = 255
        g = 0
        b = 0
        brightness = 0.1
        blinkt.clear()
        blinkt.set_all(r, g, b, brightness)
        blinkt.show()
        pass

    def off(self):
        self.logger.info("Solid Light OFF")
        blinkt.clear()
        blinkt.show()
        pass
