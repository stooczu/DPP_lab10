class Recipe:
    def __init__(self):
        self.recipes = [Recipe]

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe):
        self.recipes.remove(recipe)

    def edit_recipe(self, recipe_to_change, recipe):
        self.recipes[self.recipes.index(recipe_to_change)] = recipe
