import logging
import sys

from states import Config

if 'win32' in sys.platform:
    import light.FakeBlinkt as blinkt
if 'darwin' in sys.platform:
    import light.FakeBlinkt as blinkt
else:
    import blinkt

from light.Light import Light


class SolidLight(Light):

    def __init__(self, config={"color": Config.LightColor.RED}):
        self.logger = logging.getLogger("SolidLight")
        self.logger.info("Solid Light created{}".format(config))
        if "LEDs" in config:
            self.colors = config["LEDs"]
        else:
            self.colors = [config["color"]]
            self.logger.info("Color [{}]".format(self.colors))
        self.brightness = 1.0
        if "brightness" in config:
            self.brightness = config["brightness"]

    def on(self):
        self.logger.info("Solid Light ON color=[{}]".format(self.colors))
        blinkt.clear()

        if len(self.colors) > 1:
            self.logger.info("More than 1 color")
            for i in range(len(self.colors)):
                if self.colors[i]:
                    rgb = [int(x * 255) for x in self.colors[i].value.rgb]
                    # TODO I cannot remember what it is
                    # TODO I think I know what it is - it is a temp brightness adjustment
                    if rgb[0] == 255:
                        # TODO fix this. Change config
                        blinkt.set_pixel(7 - i, rgb[0], rgb[1], rgb[2], 0.05)
                    else:
                        blinkt.set_pixel(7 - i, rgb[0], rgb[1], rgb[2], self.brightness)
        else:
            rgb = [int(x * 255) for x in self.colors[0].rgb]
            blinkt.set_all(rgb[0], rgb[1], rgb[2], self.brightness)
        blinkt.show()
        pass

    def off(self):
        self.logger.info("Solid Light OFF")
        blinkt.clear()
        blinkt.show()
        pass
