from typing import List
from coffee_machine.container import Container
from constants.containers import AVAILABLE_CONTAINERS
from constants.menu_items import AVAILABLE_MENU_ITEMS, MenuItem
from ui.terminal import CoffeeMachineTerminalUI
from ui.ui_base import CoffeeMachineUIBase


class CoffeeMachine:
    """Represents a coffee machine."""

    def __init__(
        self,
        containers: List[Container] = AVAILABLE_CONTAINERS,
        menu_items: List[MenuItem] = AVAILABLE_MENU_ITEMS,
        ui: CoffeeMachineUIBase = CoffeeMachineTerminalUI(),
    ):
        """
        Initializes a new instance of the CoffeeMachine class.

        Args:
            containers: A list of Container objects representing the available containers.
            menu_items: A list of MenuItem objects representing the available menu items.
            ui: The user interface for the coffee machine.
        """
        self.containers = containers
        self.menu_items = menu_items
        self.threshold_in_ml = 100
        self.ui = ui

    def start(self) -> None:
        """Starts the coffee machine."""
        self.ui.print_message("Welcome to the Coffee Machine!")

        try:
            while True:
                self.check_container_quantity()
                selected_menu_item = self.select_menu_item()
                self.serve(selected_menu_item)
        except ValueError:
            self.ui.print_message("Invalid option selected")
        except Exception as e:
            self.ui.print_message(str(e))
        finally:
            self.start()

    def select_menu_item(self) -> MenuItem:
        """
        Prompts the user to select a menu item.

        Returns:
            The selected MenuItem object.

        Raises:
            ValueError: If an invalid option is selected.
        """
        self.ui.display_menu_items(self.menu_items)
        try:
            selected_option = int(self.ui.get_user_input("Enter your choice: "))
        except ValueError:
            raise ValueError("Invalid option selected")

        if not 1 <= selected_option <= len(self.menu_items):
            raise ValueError("Invalid option selected")

        selected_menu_item = self.menu_items[selected_option - 1]
        return selected_menu_item

    def check_container_quantity(self) -> None:
        """
        Checks the quantity of each container and prompts for refill if below threshold.

        Raises:
            ValueError: If an invalid option is selected.
        """
        for container in self.containers:
            if container.current_capacity_in_ml < self.threshold_in_ml:
                self.ui.print_message(
                    f"Low capacity in {container.ingredient.name} container. Please select 1 to refill"
                )
                try:
                    selected_option = int(self.ui.get_user_input("Enter your choice: "))
                except ValueError:
                    raise ValueError("Invalid option selected")
                if selected_option == 1:
                    container.refill()
                else:
                    raise ValueError("Invalid option selected")

    def serve(self, menu_item: MenuItem):
        """
        Prepares and serves the selected menu item.

        Args:
            menu_item: The MenuItem object to be served.
        """
        self.ui.print_message(f"Preparing {menu_item.name}...")
        for ingredient_quantity in menu_item.recipe:
            for container in self.containers:
                if ingredient_quantity.ingredient.name == container.ingredient.name:
                    self.ui.display_ingredient_dispensing(
                        ingredient_quantity.ingredient.name
                    )
                    self.ui.display_message_and_sleep(
                        "", ingredient_quantity.quantity * 0.01
                    )
                    container.disperse(ingredient_quantity.quantity)
        self.ui.display_ready_message(menu_item.name)
