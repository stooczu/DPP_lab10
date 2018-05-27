class Ingredient:

    def __init__(self, name, amount, unit, ingredients):
        self.name = name
        self.amount = amount
        self.unit = unit
        ingredients.ingredients.append(self)

    def __str__(self):
        return self.name + " " + self.amount + self.unit


class Ingredients:
    def __init__(self):
        self.ingredients = []
