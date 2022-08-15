import datetime
import logging

from states.Config import LightColor, LightEffect, OVERTIME, Activity, OVERTIME_ALERT
from states.AlertState import AlertState
from states.OvertimeState import OvertimeState
from states.RestState import RestState
from states.State import State


class WorkState(State):
    UNACCEPTED_DIFFERENCE = 2 * 3600

    def __init__(self, context):
        super().__init__(context)
        self.name = self.__class__.__name__
        self.logger = logging.getLogger(self.name)
        self.timer = context.get_current_time()
        self.logger.debug(f"* [{self.name}] created [{self.timer:.0f}] seconds since epoch")
        # self.context.light_on(LightEffect.SOLID_RED, {'color': LightColor.RED})

    def evaluate(self, activity) -> None:
        self.fix_timer()
        self.logger.debug("----->  WorkState:evaluate")
        if activity == Activity.IDLE:
            self.logger.info("----->  Idle activity move to rest")
            self.context.light_off()
            # Create Break state and switch
            self.context.change_state(RestState(self.context, self))
        # elif self.context.get_current_time() - self.timer > OVERTIME_ALERT:
        #     self.logger.info("----->  Working activity move to Alert state")
        #     self.context.change_state(AlertState(self.context))
        elif self.context.get_current_time() - self.timer > OVERTIME:
            self.logger.info("----->  OVERTIME[{}m] Switch to Overtime state! timer[{}],"
                             " timer+OVERTIME[{}], current time[{}]"
                             .format(round((self.context.get_current_time() - self.timer)/60), round(self.timer),
                                     round(self.timer + OVERTIME),
                                     round(self.context.get_current_time())))
            # self.context.light_on(LightEffect.SOLID_RED)
            self.context.change_state(OvertimeState(self.context))
        else:
            self.logger.info(
                "----->  Working time! Timer[{}]".format(round(self.context.get_current_time() - self.timer)))
            # self.context.light_on(LightEffect.SOLID_BLUE)
        self.logger.debug("WorkState evaluate finished")

    # when PI is turned on it looks like it starts where it stopped and the timer is set to the previous date
    def fix_timer(self):
        self.logger.debug("----->  Fix_timer")
        current_time = self.context.get_current_time()
        time_difference = current_time - self.timer
        if time_difference > self.UNACCEPTED_DIFFERENCE:
            self.logger.warning(f"[{self.name}] timer fixed from "
                                f"[{datetime.datetime.fromtimestamp(self.timer).strftime('%Y-%m-%d %H:%M:%S')}] "
                                f"to [{datetime.datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S')}]")
            self.timer = current_time
