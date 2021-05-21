from BreakState import BreakState
from Constants import Activity, OVERTIME, LightColor, LightMode
from State import State


class WorkState(State):

    workTimer = 0

    def __init__(self, context):
        super().__init__(context)
        self.workTimer = context.get_current_time()
        print(f"* WorkStare created [${self.workTimer}]")

    def evaluate(self, activity):
        if activity == Activity.IDLE:
            self.context.light_off(LightColor.RED)
            # Create Break state and switch
            self.context.change_state(BreakState(self.context, self))
        elif self.workTimer + OVERTIME < self.context.get_current_time():
            self.context.light_on(LightColor.RED, LightMode.BLINKING)
