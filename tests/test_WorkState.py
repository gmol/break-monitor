import logging
import time
from unittest import TestCase
from unittest.mock import Mock

from states.Config import Activity, OVERTIME, LightColor, LightEffect
from states.Context import Context
from light.LightController import LightController
from states.RestState import RestState
from states.TimeProvider import TimeProvider
from states.WorkState import WorkState


class TestWorkState(TestCase):

    def setUp(self):
        self.logger = logging.getLogger("TestWorkState")
        self.mock_light = Mock(spec=LightController)
        self.mock_time_provider = Mock(spec=TimeProvider)
        self.mock_time_provider.get_current_time.side_effect = [time.time(), time.time() + OVERTIME + 1]
        self.context = Context(self.mock_light, self.mock_time_provider)
        # Idle state light_controller
        self.mock_light.on.assert_called_with(LightEffect.SOLID_RED, {'color': LightColor.WHITE})
        assert self.mock_light.on.call_count == 1

    def test_evaluate_overtime(self):
        self.logger.debug("---> test_evaluate_overtime")
        working = WorkState(self.context)
        # Working state light_controller
        self.mock_light.on.assert_called_with(LightEffect.SOLID_RED, {'color': LightColor.RED})

        # It is overtime the red light_controller should blink
        working.evaluate(Activity.WORKING)
        self.mock_light.on.assert_called_with(LightEffect.BLINKING, {'color': LightColor.RED})

        assert self.mock_light.on.call_count == 3

    def test_evaluate_idle_activity(self):
        self.logger.debug("---> test_evaluate_idle_activity")
        working = WorkState(self.context)
        # Working state light_controller
        self.mock_light.on.assert_called_with(LightEffect.SOLID_RED, {'color': LightColor.RED})
        # It is overtime the red light_controller should blink
        working.evaluate(Activity.IDLE)
        self.mock_light.off.assert_called_once()
        print(f"Current state: ${self.context.state}")
        assert isinstance(self.context.state, RestState)
        pass
