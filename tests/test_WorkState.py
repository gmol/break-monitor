import logging
import time
from unittest import TestCase
from unittest.mock import Mock
from unittest.mock import call

from light.LightController import LightController
from states.Config import Activity, OVERTIME, OVERTIME_ALERT, LightEffect
from states.Context import Context
from states.RestState import RestState
from states.TimeProvider import TimeProvider
from states.WorkState import WorkState


class TestWorkState(TestCase):

    def get_current_time_with_log(self):
        """
        Logs a message and returns the current time.
        """
        # self.logger.debug(f">>>---> get_current_time method called while the state: ${self.context.state}")
        return time.time()

    def light_on_peek(self, light_mode):
        self.logger.debug(f"Mock light on: {light_mode}")

    def custom_time_provider(self, time_acceleration=OVERTIME):
        """
        This generator function yields time.time() for the first N calls,
        time.time() + OVERTIME for the N+1 call, and then time.time() for all subsequent calls.
        """

        count = 0  # Initialize a counter to keep track of the number of calls
        while True:  # Create an infinite loop so the generator never gets exhausted
            if count < 2:  # For the first two calls
                self.logger.debug(f">>>---> custom_time_provider called returns time.time()")
                yield time.time()
            else:  # For all subsequent calls
                self.logger.debug(f">>>---> custom_time_provider called returns time.time() + OVERTIME")
                yield time.time() + time_acceleration + 1
            count += 1  # Increment the counter after each call

    def setUp(self):
        self.logger = logging.getLogger("TestWorkState")
        self.logger.debug(">>>---> setUp")
        self.mock_light = Mock(spec=LightController)
        self.mock_light.light_on.side_effect = self.light_on_peek
        self.mock_time_provider = Mock(spec=TimeProvider)
        # self.mock_time_provider.get_current_time.side_effect = lambda: time.time()
        # self.mock_time_provider.get_current_time.side_effect = [time.time(), time.time() + OVERTIME + 1]
        self.mock_time_provider.get_current_time.side_effect = self.get_current_time_with_log

        self.context = Context(self.mock_light, self.mock_time_provider)
        self.logger.debug(f"Current time from timeProvider mock: ${self.context.get_current_time()}")

    def test_evaluate_idle_activity(self):
        self.logger.debug("---> test_evaluate_idle_activity")
        working = WorkState(self.context)
        working.evaluate(Activity.IDLE)
        self.mock_light.light_off.assert_called_once()
        assert isinstance(self.context.state, RestState)

    def test_evaluate_overtime(self):
        self.logger.debug("---> test_evaluate_overtime")
        self.mock_time_provider.get_current_time.side_effect = self.custom_time_provider()
        working = WorkState(self.context)
        working.fix_timer = Mock()
        # It is overtime the red light_controller should blink
        working.evaluate(Activity.WORKING)
        # when Context is created it sets the state to IdleState thus the blue light
        self.mock_light \
            .light_on.assert_has_calls([call(LightEffect.SOLID_BLUE),
                                        call(LightEffect.SOLID_RED)],
                                       any_order=True)

    def test_evaluate_alert(self):
        self.logger.debug("---> test_evaluate_alert")
        self.mock_time_provider.get_current_time.side_effect = self.custom_time_provider(OVERTIME_ALERT)
        working = WorkState(self.context)
        working.fix_timer = Mock()

        # It is overtime the red light_controller should blink
        working.evaluate(Activity.WORKING)
        # when Context is created it sets the state to IdleState thus the blue light
        self.mock_light.light_on.assert_called_with(LightEffect.BLINKING)
        self.mock_light \
            .light_on.assert_has_calls([call(LightEffect.SOLID_BLUE),
                                        call(LightEffect.BLINKING)],
                                       any_order=True)
