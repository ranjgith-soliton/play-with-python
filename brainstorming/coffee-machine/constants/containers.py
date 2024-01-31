from coffee_machine.container import Container
from models import Ingredient


coffee_container = Container(Ingredient.COFFEE)
tea_container = Container(Ingredient.TEA)
water_container = Container(Ingredient.WATER)
milk_container = Container(Ingredient.MILK)


AVAILABLE_CONTAINERS = [
    coffee_container,
    tea_container,
    water_container,
    milk_container,
]
