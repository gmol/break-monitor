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
        self.workStartTime = -1.0
        atexit.register(self.cleanup)

    def change_state(self, state):
        self.logger.info(f"-----> Change state ${state}")
        self.state = state
        # publish the state change to the mqtt if mqttNotifier is available
        if self.mqttNotifier is not None:
            self.mqttNotifier.publish_state(state)

    def update_action(self, activity: Activity):
        self.state.evaluate(activity)

    def light_on(self, light_mode, extra_config=None):
        self.light_controller.on(light_mode, extra_config)

    def light_off(self):
        self.light_controller.off()

    def get_current_time(self):
        if self.timeProvider is None:
            return time.time()
        else:
            return self.timeProvider.get_current_time()

    def cleanup(self):
        self.logger.info('Turn off the light.')
        self.light_controller.off()

    def get_work_start_time(self):
        return self.workStartTime

    def set_work_start_time_now(self):
        # self.logger.info(f"Work start time set to now ${self.timeProvider.get_current_time()}")
        self.workStartTime = self.timeProvider.get_current_time()
        self.logger.info(f"Work start time set to [{time}]")

    def get_elapsed_time(self):
        return self.get_current_time() - self.workStartTime
