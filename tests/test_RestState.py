import logging
import time
from unittest import TestCase
from unittest.mock import Mock

from colour import Color

from light.LightController import LightController
from states.Config import Activity, REST_TIME, light_config, LightEffect
from states.Context import Context
from states.IdleState import IdleState
from states.RestState import RestState
from states.TimeProvider import TimeProvider
from states.WorkState import WorkState


class TestRestState(TestCase):

    def setUp(self):
        self.logger = logging.getLogger("TestRestState")
        self.logger.debug(">>>---> setUp")

        self.mock_light = Mock(spec=LightController)
        self.mock_time_provider = Mock(spec=TimeProvider)
        self.mock_time_provider.get_current_time.side_effect = time.time

        self.context = Context(self.mock_light, self.mock_time_provider)
        self.context.mqttNotifier = Mock()

    def test_transition_to_work_state_on_working_activity(self):
        """Test RestState transitions to WorkState upon receiving a WORKING activity."""
        rest_state = RestState(self.context)
        rest_state.evaluate(Activity.WORKING)
        # Verify the transition to WorkState
        self.mock_light.light_off.assert_called()
        assert isinstance(self.context.state, WorkState)

    def test_transition_to_idle_state_after_rest_time(self):
        """Test RestState transitions to IdleState after REST_TIME has elapsed."""
        start_time = time.time()
        self.mock_time_provider.get_current_time.side_effect = [start_time, start_time + REST_TIME + 1]
        rest_state = RestState(self.context)
        self.mock_light.light_on.assert_called_with(light_config[LightEffect.REST])
        rest_state.evaluate(Activity.IDLE)
        # Verify the transition to IdleState
        self.mock_light.light_on.assert_called_with(light_config[LightEffect.IDLE])
        assert isinstance(self.context.state, IdleState)

