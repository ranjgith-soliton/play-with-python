from typing import List
from models import MenuItem
import time

from ui.ui_base import CoffeeMachineUIBase


class CoffeeMachineTerminalUI(CoffeeMachineUIBase):
    """Represents the user interface for the coffee machine."""

    @staticmethod
    def print_message(message: str):
        """Prints a message to the user interface."""
        print(message)

    @staticmethod
    def get_user_input(prompt: str) -> str:
        """Gets user input from the user interface."""
        return input(prompt)

    @staticmethod
    def display_menu_items(menu_items: List[MenuItem]):
        """Displays the available menu items to the user interface."""
        print("Please select a menu item from the following:")
        for index, menu_item in enumerate(menu_items):
            print(f"{index+1}. {menu_item.name}")

    @staticmethod
    def display_ingredient_dispensing(ingredient_name: str):
        """Displays the dispensing of an ingredient to the user interface."""
        print(f"Dispensing {ingredient_name}")

    @staticmethod
    def display_message_and_sleep(message: str, sleep_time: float):
        """Displays a message to the user interface and sleeps for a specified time."""
        print(message)
        time.sleep(sleep_time)

    @staticmethod
    def display_ready_message(menu_item_name: str):
        """Displays a ready message to the user interface."""
        print(f"Your {menu_item_name} is ready!")
