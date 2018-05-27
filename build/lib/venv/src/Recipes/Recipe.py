import src.UI.imageGenerator


class Recipe:

    def __init__(self, name, description, ingredients, recipes, image):
        self.name = name
        self.description = description
        self.image = image
        self.rating = "Not rated"
        self.ingredients = ingredients
        self.noVoices = 0
        self.comments = []
        recipes.recipes.append(self)

    def add_ingredients(self, recipes):
        self.recipes.append(recipes)

    def add_comment(self, comment):
        self.comments.append(comment)

    def __str__(self):
        src.UI.imageGenerator.printImage("./" + self.image)
        print(*self.ingredients.ingredients, sep='\n')
        string = self.name + "\n" + self.description + "\n"
        if self.noVoices <= 0:
            string += "Not rated"
        elif self.noVoices > 0:
            string += str(self.get_rate())
        return string

    def rate(self, rate):
        if self.noVoices == 0:
            self.rating = 0
        self.noVoices = self.noVoices + 1
        self.rating = self.rating + rate

    @staticmethod
    def del_recipe(index, recipes):
        del recipes[index]

    def get_rate(self):

        return self.rating / self.noVoices


class Recipes:

    def __init__(self):
        self.recipes = []
