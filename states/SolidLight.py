import blinkt
from states.Light import Light


class SolidLight(Light):

    def on(self, config={}):
        r = 255
        g = 0
        b = 0
        brightness = 0.1

        blinkt.set_all(r, g, b, brightness)

    def off(self):
        blinkt.clear()
