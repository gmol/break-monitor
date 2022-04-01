import logging
import paho.mqtt.publish as publish

from states.Config import MqttConfig
from states.State import State


class MqttNotifier:

    def __init__(self):
        self.logger = logging.getLogger("MqttNotifier")

    def publish_state(self, state: State):
        payload = state.__class__.__name__
        self.logger.info(f"Publish state [{payload}] to MQTT topic [{MqttConfig.TOPIC}] to broken [{MqttConfig.HOST}]")
        publish.single(MqttConfig.TOPIC, payload, hostname=MqttConfig.HOST)
