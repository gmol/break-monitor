import logging
import time
from unittest import TestCase
from unittest.mock import ANY
from unittest.mock import Mock
from unittest.mock import patch

from light.LightController import LightController
from states.Config import LightEffect, Activity
from states.Context import Context
from states.IdleState import IdleState
from states.TimeProvider import TimeProvider
from states.WorkState import WorkState


class TestIdleState(TestCase):

    def get_current_time_with_log(self):
        """
        Logs a message and returns the current time.
        """
        # self.logger.debug(f">>>---> get_current_time method called while the state: ${self.context.state}")
        return time.time()

    def setUp(self):
        self.logger = logging.getLogger("TestIdleState")

        self.mock_light = Mock(spec=LightController)
        self.mock_time_provider = Mock(spec=TimeProvider)
        # self.mock_time_provider.get_current_time.side_effect = [time.time(), time.time() + 1]
        self.mock_time_provider.get_current_time.side_effect = self.get_current_time_with_log
        self.context = Context(self.mock_light, self.mock_time_provider)
        assert isinstance(self.context.state, IdleState)
        self.context.mqttNotifier = Mock()

    def test_evaluate_working(self):
        with patch.object(self.context, 'change_state', wraps=self.context.change_state) as contextSpy:
            idle_state = IdleState(self.context)
            idle_state.evaluate(Activity.WORKING)
            self.mock_light.off.assert_called_once()
            assert isinstance(self.context.state, WorkState)
            contextSpy.assert_called_once()

    def test_evaluate_idle(self):
        idle_state = IdleState(self.context)
        idle_state.evaluate(Activity.IDLE)
        self.mock_light.on.assert_called_with(LightEffect.SOLID_ARBITRARY, ANY)


