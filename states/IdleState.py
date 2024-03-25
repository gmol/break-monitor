import logging
import sys
from socket import socket
from time import sleep

from helpers.ip_address import get_last_ip_number_in_bin_array
from states import Config
from states.Config import LightEffect, LightColor, Activity
# from states.Context import Context
from states.State import State


class IdleState(State):
    NUMBER_OF_TRIES = 30

    def __init__(self, context):
        super().__init__(context)
        self.logger = logging.getLogger("IdleState")
        self.logger.info("* IdleState created")
        self.context.reset_work_start_time()
        self._light_config = Config.light_config[LightEffect.SOLID_BLUE]
        self.context.get_light_controller().light_on(self._light_config)

    def evaluate(self, activity: Activity) -> None:
        if activity == Activity.WORKING:
            self.logger.info("Working activity move to WorkState")
            # Create Work state and switch
            from states.WorkState import WorkState
            self.context.change_state(WorkState(self.context))
        elif activity == Activity.IDLE:
            self.logger.info("Idle activity")
            self.logger.info("SELECTED SOLID light config {}".format(self._light_config))
            self.context.get_light_controller().light_on(self._light_config)
