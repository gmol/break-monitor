from Constants import Activity, REST_TIME
from IdleState import IdleState
from State import State


class BreakState(State):
    timer = 0

    def __init__(self, context, work_state):
        super().__init__(context)
        self.nextState = work_state
        print("* BreakState created")
        self.timer = self.context.get_current_time()

    def evaluate(self, activity):
        if activity == Activity.WORKING:
            # TODO This might be optional. Do not come back to WorkState after the break started
            # You can avoid false work comebacks if you break is near the desk
            # Unless the activity evaluation exclude near desk presence as working time
            self.context.change_state(self.nextState)
        if self.timer + REST_TIME < self.context.get_current_time():
            # Create Idle state and switch
            self.context.change_state(IdleState(self.context))
