import logging
import time
import atexit

from light.LightController import LightController
from mqtt import MqttNotifier
from states.Config import Activity
from states.IdleState import IdleState


class Context:

    def __init__(self, light_controller: LightController, time_provider=None, mqtt_notifier: MqttNotifier = None):
        self.logger = logging.getLogger("Context")
        self.light_controller = light_controller
        self.state = IdleState(self)
        self.timeProvider = time_provider
        self.mqttNotifier = mqtt_notifier
        atexit.register(self.cleanup)

    def change_state(self, state):
        self.logger.info(f"-----> Change state ${state}")
        self.state = state
        self.mqttNotifier.publish_state(state)

    def update_action(self, activity: Activity):
        # print(f"-----> change state ${activity}")
        # print(f"-----> change state ${Activity.WORKING}")
        # if activity == Activity.WORKING:
        #     print(f"Update activity ${activity} and ${Activity.WORKING} are ==")
        # else:
        #     print(f"Update activity ${activity} and ${Activity.WORKING} are !=")
        # self.logger.debug(f"Update activity ${activity}")
        self.state.evaluate(activity)

    def light_on(self, light_mode, extra_config=None):
        self.logger.info(f"-----> light on")
        self.light_controller.on(light_mode, extra_config)

    def light_off(self):
        self.light_controller.off()

    # Returns time in seconds
    def get_current_time(self):
        # self.logger.debug(f"-----> get_current_time")
        if self.timeProvider is None:
            # self.logger.debug(f"-----> time.time()")
            return time.time()
        else:
            self.logger.\
                debug(f'---> self.timeProvider.get_current_time() [{self.timeProvider.get_current_time():.0f}] seconds '
                      f'since epoch')
            return self.timeProvider.get_current_time()

    def cleanup(self):
        self.logger.info('Turn off the light.')
        self.light_controller.off()

    def get_state(self):
        return self.state
