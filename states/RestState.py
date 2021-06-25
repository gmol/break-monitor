import logging

from states.Config import LightEffect, LightColor, Activity, REST_TIME
from states.IdleState import IdleState
from states.State import State


class RestState(State):

    def __init__(self, context, work_state):
        super().__init__(context)
        self.logger = logging.getLogger("RestState")
        self.nextState = work_state
        self.logger.info("* RestState created")
        self.timer = self.context.get_current_time()
        self.context.light_on(LightEffect.SOLID_GREEN)

    def evaluate(self, activity):
        if activity == Activity.WORKING:
            self.logger.info("working move to WorkState")
            # TODO This might be optional. Do not come back to WorkState after the break started
            # You can avoid false work comebacks if you rest time is near the desk
            # Unless the activity evaluation exclude near desk presence as working time

            # Adjust the working state timer by deducting a 'short' break time
            self.nextState.adjust_timer(-self.context.get_current_time() + self.timer)
            self.context.light_off()
            self.context.change_state(self.nextState)
            pass
        if self.timer + REST_TIME < self.context.get_current_time():
            self.logger.info("Activity[{}] rest finish move to Idle state".format(activity))
            # Create Idle state and switch
            self.context.light_off()
            self.context.change_state(IdleState(self.context))
            pass
        self.logger.info("Activity[{}] resting. Timer[{}]"
                         .format(activity, round(self.context.get_current_time() - self.timer)))
        self.context.light_on(LightEffect.SOLID_GREEN)
