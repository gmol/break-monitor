from Constants import Activity, LightMode, LightColor
from State import State


class IdleState(State):
    def __init__(self, context):
        super().__init__(context)
        print("* IdleState created")
        self.context.light_on(LightColor.GREEN, LightMode.SOLID)

    def evaluate(self, activity) -> None:
        if activity == Activity.WORKING:
            self.context.light_off(LightColor.GREEN)
            # Create Work state and switch
            from WorkState import WorkState
            self.context.change_state(WorkState(self.context))
        elif activity == Activity.IDLE:
            self.context.light_on(LightColor.GREEN, LightMode.SOLID)
