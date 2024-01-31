from dataclasses import dataclass
from enum import Enum

from models.ingredient import Ingredient


@dataclass
class IngredientQuantity:
    ingredient: Ingredient
    quantity: int


class MenuItemName(str, Enum):
    COFFEE = "Coffee"
    STRONG_COFFEE = "Strong Coffee"
    BLACK_COFFEE = "Black Coffee"
    TEA = "Tea"
    STRONG_TEA = "Strong Tea"
    BLACK_TEA = "Black Tea"

    def __str__(self) -> str:
        return str.__str__(self)


@dataclass
class MenuItem:
    name: MenuItemName
    recipe: list[IngredientQuantity]