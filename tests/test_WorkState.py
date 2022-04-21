import logging
import time
from unittest import TestCase
from unittest.mock import Mock

from mqtt.MqttNotifier import MqttNotifier
from states.Config import Activity, OVERTIME, LightColor, LightEffect
from states.Context import Context
from light.LightController import LightController
from states.RestState import RestState
from states.TimeProvider import TimeProvider
from states.WorkState import WorkState


class TestWorkState(TestCase):

    initial_time = time.time()
    timer_call_counter = 0
    logger = logging.getLogger("TestWorkState")

    def next_timer_value(self):
        if self.timer_call_counter == 1:
            self.logger.debug(f'---> next_timer_value add OVERTIME')
            self.initial_time = self.initial_time + OVERTIME + 1
        else:
            self.initial_time += 1000

        self.logger.debug(f'---> next_timer_value[{self.timer_call_counter}]=[{self.initial_time:.0f}]')
        self.timer_call_counter = self.timer_call_counter + 1
        return self.initial_time

    def setUp(self):
        self.logger.info(f'Get logger level [{self.logger.getEffectiveLevel()}] [{logging.DEBUG}] [{logging.INFO}] '
                         f' [{logging.ERROR}]')
        self.mock_light = Mock(spec=LightController)
        self.mock_time_provider = Mock(spec=TimeProvider)
        self.mock_time_provider.get_current_time.side_effect = self.next_timer_value
        self.mock_mqtt = Mock(spec=MqttNotifier)
        self.context = Context(light_controller=self.mock_light,
                               time_provider=self.mock_time_provider,
                               mqtt_notifier=self.mock_mqtt)
        # Idle state light_controller
        # self.mock_light.on.assert_called_with(LightEffect.SOLID_RED, {'color': LightColor.WHITE})
        # assert self.mock_light.on.call_count == 1

    def test_evaluate_overtime(self):
        self.logger.debug("---> test_evaluate_overtime")
        working = WorkState(self.context)
        # Working state light_controller
        self.mock_light.on.assert_called_with(LightEffect.SOLID_RED)

        # It is overtime the red light_controller should blink
        working.evaluate(Activity.WORKING)
        self.mock_light.on.assert_called_with(LightEffect.SOLID_RED)

        assert self.mock_light.on.call_count == 3

    def test_evaluate_idle_activity(self):
        self.logger.debug("---> test_evaluate_idle_activity")
        working = WorkState(self.context)

        # It is idle state so the state should be switched to Rest
        working.evaluate(Activity.IDLE)

        # Rest state should turn on green light
        self.mock_light.on.assert_called_with(LightEffect.SOLID_GREEN, None)

        self.mock_light.off.assert_called_once()
        print(f"Current state: ${self.context.state}")
        assert isinstance(self.context.state, RestState)
        pass
