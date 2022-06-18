import time
import unittest
import logging
from unittest.mock import Mock

from light.LightController import LightController
from mqtt.MqttNotifier import MqttNotifier
from states.AlertState import AlertState
from states.TimeProvider import TimeProvider
from states.Config import Activity, LightEffect, OVERTIME_ALERT, OVERTIME
from states.Context import Context
from states.OvertimeState import OvertimeState
from states.RestState import RestState
from states.WorkState import WorkState


class TestOvertimeState(unittest.TestCase):
    logger = logging.getLogger("TestOvertimeState")

    test_start = time.time()
    initial_time = test_start
    timer_call_counter = 0  # TODO It does not have functional value. It's only for debugging. remove in future
    time_accelerator = 0

    def setUp(self):
        self.logger.info(f'Setup test. Get logger level[{self.logger.getEffectiveLevel()}] DEBUG[{logging.DEBUG}]'
                         f' INFO[{logging.INFO}] '
                         f' ERROR[{logging.ERROR}]')
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
        self.reset_timer_call_counter()

    def next_timer_value(self):
        # self.logger.debug(f'---> next_timer_value:Start')
        # if self.get_timer_call_counter() == 1:
        # self.logger.debug(f'---> next_timer_value [Add OVERTIME]')
        self.initial_time = self.initial_time + self.get_time_acceleration() + 1
        # else:
        #     self.initial_time += 1000

        self.logger.debug(
            f'---> next_timer_value [{self.get_timer_call_counter()}]=[{self.initial_time - self.test_start:.0f}] '
            f'seconds since test start')
        self.incr_timer_call_counter()
        return self.initial_time

    def get_time_acceleration(self):
        tmp = self.time_accelerator
        self.time_accelerator = 0
        return tmp

    def set_time_acceleration(self, delta):
        self.time_accelerator = delta

    def get_timer_call_counter(self):
        # self.logger.info(f'Get counter [{self.timer_call_counter}]')
        return self.timer_call_counter

    def incr_timer_call_counter(self):
        # self.logger.info(f'Incr counter [{self.timer_call_counter}]->[{self.timer_call_counter + 1}]')
        self.timer_call_counter = self.timer_call_counter + 1
        return self.timer_call_counter

    def reset_timer_call_counter(self):
        # self.logger.info(f'Reset counter [{0}]')
        self.timer_call_counter = 0

    def test_evaluate_idle_activity(self):
        self.logger.debug(">>>---> test_evaluate_idle_activity")
        working = OvertimeState(self.context)

        # It is idle state so the state should be switched to Rest
        working.evaluate(Activity.IDLE)

        # Rest state should turn on green light
        self.mock_light.on.assert_called_with(LightEffect.SOLID_GREEN, None)

        self.mock_light.off.assert_called_once()
        # self.context.change_state.assert_called_once()
        assert isinstance(self.context.state, RestState)
        pass

    def test_evaluate_working_activity(self):
        self.logger.debug(">>>---> test_evaluate_working_activity")
        # Move from Idle -> Work
        self.context.update_action(Activity.WORKING)
        assert isinstance(self.context.state, WorkState)

        self.set_time_acceleration(OVERTIME)
        # Move from Work -> Overtime
        self.context.update_action(Activity.WORKING)
        assert isinstance(self.context.state, OvertimeState)
        # OvertimeState should turn on red light
        self.mock_light.on.assert_called_with(LightEffect.SOLID_RED, None)

        # Keep working as Overtime
        self.context.update_action(Activity.WORKING)
        assert isinstance(self.context.state, OvertimeState)

        # OvertimeState should turn on red light
        self.mock_light.on.assert_called_with(LightEffect.SOLID_RED, None)
        pass

    def test_evaluate_alert_activity(self):
        self.logger.debug(">>>---> test_evaluate_working_activity")
        # Move from Idle -> Work
        self.context.update_action(Activity.WORKING)
        assert isinstance(self.context.state, WorkState)

        self.set_time_acceleration(OVERTIME)
        # Move from Work -> Overtime
        self.context.update_action(Activity.WORKING)
        assert isinstance(self.context.state, OvertimeState)

        # Accelerate time to Alert state
        self.set_time_acceleration(OVERTIME_ALERT)

        # Keep working as Overtime
        self.context.update_action(Activity.WORKING)
        assert isinstance(self.context.state, AlertState)

        # OvertimeState should turn on green light
        self.mock_light.on.assert_called_with(LightEffect.BLINKING, None)

        pass
