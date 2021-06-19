import logging
from socket import socket

from helpers.ip_address import get_last_ip_number_in_bin_array
from states import Config
from states.Config import LightEffect, LightColor, Activity
from states.State import State


class IdleState(State):

    def __init__(self, context):
        super().__init__(context)
        self.logger = logging.getLogger("IdleState")
        self.logger.info("* IdleState created")
        self.ip_bits = get_last_ip_number_in_bin_array()
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
