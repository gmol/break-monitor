import datetime
import logging

import states.RestState
from states.Config import LightEffect, OVERTIME, Activity, OVERTIME_ALERT
from states.Context import Context
from states.State import State
from states import Config


class WorkState(State):
    UNACCEPTED_DIFFERENCE = 2 * 3600

    def __init__(self, context: Context):
        super().__init__(context)
        self.logger = logging.getLogger("WorkState")
        self.timer = context.get_current_time()
        self.logger.debug(f"* WorkStare created [${self.timer}]")
        if context.get_work_start_time() <= 0:
            context.set_work_start_time_now()
        self.context.get_light_controller().light_off()

    def evaluate(self, activity: Activity) -> None:
        self.logger.debug(f"WorkState evaluate")
        self.fix_timer()
        elapsed_time = self.context.get_elapsed_time()
        current_time = self.context.get_current_time()
        self.logger.debug(f"WorkState evaluate after fix_timer, elapsed time: {elapsed_time}")
        if activity == Activity.IDLE:
            self.logger.info("----->  Idle activity move to rest")
            # Create Break state and switch
            self.context.change_state(states.RestState.RestState(self.context))
        elif elapsed_time > OVERTIME:
            self.logger.info("----->  OVERTIME [{}m] turn the alarm on! work time[{}], current time[{}]"
                             .format(round(elapsed_time / 60),
                                     round(self.context.get_work_start_time()),
                                     round(current_time)))
            if elapsed_time > OVERTIME_ALERT:
                self.logger.info("----->  OVERTIME ALERT [{}m] turn the alarm on! work time[{}], current time[{}]"
                                 .format(round(elapsed_time / 60),
                                         round(self.context.get_work_start_time()),
                                         round(current_time)))
                light_config = Config.light_config[LightEffect.BLINKING]
                self.context.get_light_controller().light_on(light_config)
            else:
                light_config = Config.light_config[LightEffect.SOLID_RED]
                self.context.get_light_controller().light_on(light_config)
        else:
            self.logger.info(
                "----->  Working time! Timer[{}]".format(round(elapsed_time)))

    # TODO double check this. it might be not necessary as I improve timer handling
    # when PI is turned on it looks like it starts where it stopped and the timer is set to the previous date
    def fix_timer(self):
        self.logger.debug(f"WorkState timer fix")
        current_time = self.context.get_current_time()
        start_time = self.context.get_work_start_time()
        time_difference = current_time - start_time
        if time_difference > self.UNACCEPTED_DIFFERENCE:
            self.logger.warning(
                f"WorkState timer fixed from "
                f"[{datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')}]"
                f"to [{datetime.datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S')}]"
            )
            self.context.set_work_start_time_now()
