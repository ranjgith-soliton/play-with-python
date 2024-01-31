from models import IngredientQuantity, Ingredient, MenuItem, MenuItemName


coffee_recipe = [
    IngredientQuantity(Ingredient.MILK, 80),
    IngredientQuantity(Ingredient.COFFEE, 20),
]
strong_coffee_recipe = [
    IngredientQuantity(Ingredient.MILK, 70),
    IngredientQuantity(Ingredient.COFFEE, 30),
]
black_coffee_recipe = [
    IngredientQuantity(Ingredient.WATER, 80),
    IngredientQuantity(Ingredient.COFFEE, 20),
]
tea_recipe = [
    IngredientQuantity(Ingredient.MILK, 80),
    IngredientQuantity(Ingredient.TEA, 20),
]
strong_tea_recipe = [
    IngredientQuantity(Ingredient.MILK, 70),
    IngredientQuantity(Ingredient.TEA, 30),
]
black_tea_recipe = [
    IngredientQuantity(Ingredient.WATER, 80),
    IngredientQuantity(Ingredient.TEA, 20),
]

coffee = MenuItem(MenuItemName.COFFEE, coffee_recipe)
strong_coffee = MenuItem(MenuItemName.STRONG_COFFEE, strong_coffee_recipe)
black_coffee = MenuItem(MenuItemName.BLACK_COFFEE, black_coffee_recipe)
tea = MenuItem(MenuItemName.TEA, tea_recipe)
strong_tea = MenuItem(MenuItemName.STRONG_TEA, strong_tea_recipe)
black_tea = MenuItem(MenuItemName.BLACK_TEA, black_tea_recipe)

AVAILABLE_MENU_ITEMS = [coffee, strong_coffee, black_coffee, tea, strong_tea, black_tea]
