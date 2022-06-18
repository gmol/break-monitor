import datetime
import logging

from states.Config import LightColor, LightEffect, OVERTIME, Activity, OVERTIME_ALERT
from states.RestState import RestState
from states.AlertState import AlertState
from states.State import State


class OvertimeState(State):

    def __init__(self, context):
        super().__init__(context)
        self.name = self.__class__.__name__
        self.logger = logging.getLogger(self.name)
        self.timer = context.get_current_time()
        self.logger.debug(f"* [{self.name}] created [{self.timer:.0f}] seconds")
        self.context.light_on(LightEffect.SOLID_RED)

    def evaluate(self, activity) -> None:
        if activity == Activity.IDLE:
            self.logger.info("----->  Idle activity move to rest")
            self.context.light_off()
            # Create Break state and switch
            self.context.change_state(RestState(self.context, self))
        else:
            if self.context.get_current_time() - self.timer > OVERTIME_ALERT:
                print('Change state to AlertState')
                # self.context.light_off() # TODO maybe light off
                self.context.change_state(AlertState(self.context))
            else:
                self.context.light_on(LightEffect.SOLID_RED)
                self.logger.info(
                    "----->  Overtime! Timer[{}]".format(round(self.context.get_current_time() - self.timer)))
