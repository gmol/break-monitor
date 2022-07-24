import logging
import paho.mqtt.publish as publish

from states.Config import MqttConfig
from states.State import State


class MqttNotifier:

    def __init__(self):
        self.logger = logging.getLogger("MqttNotifier")

    def publish_state(self, state: State):
        if MqttConfig.PASSWORD:
            payload = state.__class__.__name__
            self.logger.info(f"Publish state [{payload}] to MQTT topic [{MqttConfig.TOPIC}] "
                             f"to broker [{MqttConfig.HOST}], username[{MqttConfig.USERNAME}],"
                             f" password[{MqttConfig.PASSWORD}] ")
            auth = {"username": MqttConfig.USERNAME, "password": MqttConfig.PASSWORD}

            try:
                publish.single(MqttConfig.TOPIC, payload, hostname=MqttConfig.HOST, auth=auth)
            except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                self.logger.error(message)
                self.logger.exception(ex)
                self.logger.error(f"Publish state [{payload}] to MQTT topic [{MqttConfig.TOPIC}] "
                                  f"to broker [{MqttConfig.HOST}], username[{MqttConfig.USERNAME}],"
                                  f" password[{MqttConfig.PASSWORD}] failed!")
                pass
        else:
            self.logger.info("MQTT password not set. Skip publishing to MQTT.")
