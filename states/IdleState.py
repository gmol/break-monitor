import logging

from states.Constants import LightEffect, LightColor, Activity
from states.State import State


class IdleState(State):
    def __init__(self, context):
        super().__init__(context)
        self.logger = logging.getLogger("IdleState")
        self.logger.info("* IdleState created")
        self.context.light_on(LightEffect.SOLID_WHITE)
        # self.context.light_on(LightEffect.SOLID_RED, {'color':  LightColor.WHITE})

    def evaluate(self, activity) -> None:
        if activity == Activity.WORKING:
            self.context.light_off()
            # Create Work state and switch
            from states.WorkState import WorkState
            self.context.change_state(WorkState(self.context))
        elif activity == Activity.IDLE:
            self.context.light_on(LightEffect.SOLID_GREEN)
