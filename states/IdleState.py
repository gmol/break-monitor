import logging
import sys
from socket import socket
from time import sleep

from helpers.ip_address import get_last_ip_number_in_bin_array
from states import Config
from states.Config import LightEffect, LightColor, Activity
from states.State import State


class IdleState(State):

    NUMBER_OF_TRIES = 30

    def __init__(self, context):
        super().__init__(context)
        self.logger = logging.getLogger("IdleState")
        self.logger.info("* IdleState created")
        counter = 0
        while counter < self.NUMBER_OF_TRIES:
            try:
                sleep(1)
                self.ip_bits = get_last_ip_number_in_bin_array()
                break
            except:
                counter += 1
                e = sys.exc_info()[0]
                self.logger.info('Get IP exception: {}'.format(e))

        self.effect_config = Config.light_config[LightEffect.SOLID_ARBITRARY]
        leds = [LightColor.YELLOW for i in range(8)]
        for i in range(len(self.ip_bits)):
            if 1 == self.ip_bits[i]:
                leds[i] = LightColor.BLUE

        self.effect_config["LEDs"] = leds

    def evaluate(self, activity) -> None:
        if activity == Activity.WORKING:
            self.logger.info("Working activity move to WorkState")
            self.context.light_off()
            # Create Work state and switch
            from states.WorkState import WorkState
            self.context.change_state(WorkState(self.context))
        elif activity == Activity.IDLE:
            self.logger.info("Idle activity")
            self.logger.info("SELECTED SOLID light config {}".format(self.effect_config))
            self.context.light_on(LightEffect.SOLID_ARBITRARY, self.effect_config)
