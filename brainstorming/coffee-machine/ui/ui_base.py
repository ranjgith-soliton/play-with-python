from abc import ABC, abstractmethod
from typing import List

from models import MenuItem


class CoffeeMachineUIBase(ABC):
    """Represents the user interface for the coffee machine."""

    @staticmethod
    @abstractmethod
    def print_message(message: str):
        """Prints a message to the user interface."""
        pass

    @staticmethod
    @abstractmethod
    def get_user_input(prompt: str) -> str:
        """Gets user input from the user interface."""
        pass

    @staticmethod
    @abstractmethod
    def display_menu_items(menu_items: List[MenuItem]):
        """Displays the available menu items to the user interface."""
        pass

    @staticmethod
    @abstractmethod
    def display_ingredient_dispensing(ingredient_name: str):
        """Displays the dispensing of an ingredient to the user interface."""
        pass

    @staticmethod
    @abstractmethod
    def display_message_and_sleep(message: str, sleep_time: float):
        """Displays a message to the user interface and sleeps for a specified time."""
        pass

    @staticmethod
    @abstractmethod
    def display_ready_message(menu_item_name: str):
        """Displays a ready message to the user interface."""
        pass

