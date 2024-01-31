from coffee_machine import CoffeeMachine
from pytest import fixture
import pytest

# Basic test


class TestCoffeeMachine:
    def test_coffee_machine_init(self):
        coffee_machine = CoffeeMachine()
        assert coffee_machine is not None
