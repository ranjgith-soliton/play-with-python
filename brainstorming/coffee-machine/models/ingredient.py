from enum import Enum
from dataclasses import dataclass


class Ingredient(str, Enum):
    COFFEE = "Coffee"
    TEA = "Tea"
    WATER = "Water"
    MILK = "Milk"

    def __str__(self) -> str:
        return str.__str__(self)


@dataclass
class IngredientQuantity:
    ingredient: Ingredient
    quantity: int
