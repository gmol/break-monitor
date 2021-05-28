from unittest import TestCase
from unittest.mock import Mock

from states.Constants import LightMode, Activity, LightColor
from states.Context import Context
from states.IdleState import IdleState
from states.Light import Light
from states.TimeProvider import TimeProvider
from states.WorkState import WorkState


class TestIdleState(TestCase):
    def setUp(self):
        self.mock_light = Mock(spec=Light)
        self.context = Context(self.mock_light)
        # Idle state light
        self.mock_light.on.assert_called_with(LightMode.SOLID, {'color': LightColor.WHITE})
        assert self.mock_light.on.call_count == 1

    def test_evaluate_working(self):
        idle_state = IdleState(self.context)
        idle_state.evaluate(Activity.WORKING)
        self.mock_light.off.assert_called_once()
        assert isinstance(self.context.state, WorkState)

    def test_evaluate_idle(self):
        idle_state = IdleState(self.context)
        idle_state.evaluate(Activity.IDLE)
        self.mock_light.on.assert_called_with(LightMode.SOLID, {'color': LightColor.WHITE})
        assert isinstance(self.context.state, IdleState)
