from models import Ingredient


class Container:
    """
    Represents a container that holds a specific ingredient.

    Args:
        ingredient (Ingredient): The ingredient stored in the container.
        maximum_capacity_in_ml (int, optional): The maximum capacity of the container in milliliters. Defaults to 1000.

    Attributes:
        ingredient (Ingredient): The ingredient stored in the container.
        maximum_capacity_in_ml (int): The maximum capacity of the container in milliliters.
        current_capacity_in_ml (int): The current capacity of the container in milliliters.

    """

    def __init__(self, ingredient: Ingredient, maximum_capacity_in_ml: int = 1000):
        self.ingredient = ingredient
        self.maximum_capacity_in_ml = maximum_capacity_in_ml
        self.current_capacity_in_ml = 0

    def refill(self):
        """
        Refills the container to its maximum capacity.
        """
        self.current_capacity_in_ml = self.maximum_capacity_in_ml

    def disperse(self, quantity_in_ml: int):
        """
        Disperses a specified quantity of the ingredient from the container.

        Args:
            quantity_in_ml (int): The quantity of the ingredient to disperse in milliliters.
        """
        self.current_capacity_in_ml -= quantity_in_ml
