import logging

from states.Constants import LightColor, LightMode, OVERTIME, Activity
from states.RestState import RestState
from states.State import State


class WorkState(State):

    def __init__(self, context):
        super().__init__(context)
        self.logger = logging.getLogger("WorkState")
        self.timer = context.get_current_time()
        self.logger.debug(f"* WorkStare created [${self.timer}]")
        self.context.light_on(LightMode.SOLID, {'color': LightColor.RED})

    def evaluate(self, activity):
        if activity == Activity.IDLE:
            self.context.light_off()
            # Create Break state and switch
            self.context.change_state(RestState(self.context, self))
        elif self.timer + OVERTIME < self.context.get_current_time():
            self.context.light_on(LightMode.BLINKING, {'color': LightColor.RED})
