import time


class Context:

    def __init__(self, light, time_provider=None):
        from IdleState import IdleState
        self.light = light
        self.state = IdleState(self)
        self.timeProvider = time_provider

    def change_state(self, state):
        print(f"-----> change state ${state}")
        self.state = state

    def update_action(self, activity):
        print(f"Update activity ${activity}")
        self.state.evaluate(activity)

    def light_on(self, light_color, light_mode):
        print(f"${light_color} light ON with ${light_mode} mode")
        self.light.on(light_color, light_mode)

    def light_off(self, light_color):
        print(f"${light_color} light OFF")
        self.light.off(light_color)

    def get_current_time(self):
        if self.timeProvider is None:
            return time.time()
        else:
            return self.timeProvider.get_current_time()
