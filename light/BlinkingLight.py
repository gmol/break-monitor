import logging
import sys
import time
from threading import Event, Thread

from states import Config

# if 'win32' in sys.platform:
#     import light.FakeBlinkt as blinkt
# if 'darwin' in sys.platform:
#     import light.FakeBlinkt as blinkt
# else:
#     import blinkt

from light.Light import Light


class BlinkingLight(Light):

    def __init__(self, config):
        self.worker: Thread = None
        self.stopThread = None
        self.LEDs = []
        self.logger = logging.getLogger("BlinkingLight")
        self.logger.info("Blinking Light created{}".format(config))

        if "ledConfig" in config:
            self.LEDs = config["ledConfig"]
        else:
            self.logger.info("Color [{}]".format(self.LEDs))
            for i in range(8):
                self.LEDs.append({
                    "color": config["color"],
                    "brightness": config["brightness"]
                })

    def on(self):
        self.logger.info("Solid Light ON color=[{}]".format(self.LEDs))
        # blinkt.clear()
        self.stopThread = self.call_repeatedly(0.1, self.effect)

    def effect(self):
        # self.logger.info("Blinking effect. LEDs.length=[{}]".format(len(self.LEDs)))
        assert len(self.LEDs) == 8, f'len(self.LEDs) > 8 and is [{len(self.LEDs)}]'
        # for i in range(len(self.LEDs)):
        #     if self.LEDs[i]:
        #         rgb = [int(x * 255) for x in self.LEDs[i]['color'].rgb]
        #         blinkt.set_pixel(7 - i, rgb[0], rgb[1], rgb[2], self.LEDs[i]['brightness'])
        # blinkt.show()
        # time.sleep(10)
        # blinkt.clear()
        # blinkt.show()
        # time.sleep(0.1)
        # self.logger.info("Blinking effect - 1blinked")

    def off(self):
        self.logger.info("Solid Light OFF")
        # TODO I am not sure if that it work (the IF statement I mean)
        # if 'win32' not in sys.platform:
        #     import RPi.GPIO as GPIO
        #     GPIO.setmode(GPIO.BCM)
        #     GPIO.setwarnings(False)
        self.stop_worker()
        # blinkt.clear()
        # blinkt.show()

    def stop_worker(self):
        if self.stopThread and self.worker:
            self.stopThread()
            self.worker.join()

    def call_repeatedly(self, interval, func, *args):
        self.logger.info("* call_repeatedly interval [{}]".format(interval))
        stopped = Event()

        def loop():
            while not stopped.wait(interval):  # the first call is in `interval` secs
                # self.logger.info(f"Thread's loop: ${func}")
                func(*args)

        self.worker = Thread(target=loop)
        self.worker.start()
        return stopped.set
