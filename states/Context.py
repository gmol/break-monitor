import logging
import time

from states.Constants import Activity
from states.IdleState import IdleState


class Context:

    def __init__(self, light, time_provider=None):
        self.logger = logging.getLogger("Context")
        self.light = light
        self.state = IdleState(self)
        self.timeProvider = time_provider

    def change_state(self, state):
        self.logger.info(f"-----> Change state ${state}")
        self.state = state

    def update_action(self, activity):
        # print(f"-----> change state ${activity}")
        # print(f"-----> change state ${Activity.WORKING}")
        # if activity == Activity.WORKING:
        #     print(f"Update activity ${activity} and ${Activity.WORKING} are ==")
        # else:
        #     print(f"Update activity ${activity} and ${Activity.WORKING} are !=")
        self.logger.debug(f"Update activity ${activity}")
        self.state.evaluate(activity)

    def light_on(self, light_mode, config):
        self.logger.debug(f"${config} light ON with ${light_mode} mode")
        self.light.on(light_mode, config)

    def light_off(self):
        self.logger.info(f"light OFF")
        self.light.off()

    def get_current_time(self):
        if self.timeProvider is None:
            return time.time()
        else:
            return self.timeProvider.get_current_time()
