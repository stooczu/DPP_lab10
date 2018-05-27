import os

from src.Recipes import Ingredient, Recipe, RecipesManager

allIngredients = []
recipes = Recipe.Recipes()


def clear_screen222222():
    os.system('cls' if os.name == 'nt' else 'clear')


def del_recipe():
    if len(recipes.recipes) > 0:
        print("Choose recipe to delete\n")
        print([o.name for o in recipes.recipes])
        recipe = input()
        temp = recipes.recipes[int(recipe)]
        temp.del_recipe(int(recipe), recipes.recipes)
    else:
        print("No recipes!")
        input()


def edit_recipe():
    if len(recipes.recipes) > 0:
        print("Choose recipe to edit\n")
        print([o.name for o in recipes.recipes])
        inp = input()
        temp_rep = recipes.recipes[int(inp)]
        print("What do you want to edit ?\n1.Name\n2.Description\n"
              "3.Ingredients\n4.Image")
        choice = input()
        if int(choice) == 1:
            print(temp_rep.name)
            print("Type new name:")
            new_name = input()
            temp_rep.name = new_name
        elif int(choice) == 2:
            print(temp_rep.description)
            print("Type new description:")
            new_desc = input()
            temp_rep.description = new_desc
        elif int(choice) == 3:
            print("Not implemented yet")
        elif int(choice) == 4:
            print(temp_rep.image)
            print("Type new image path:")
            new_img = input()
            temp_rep.image = new_img
    else:
        print("No recipes!")
        input()


def new_recipe2222():
    clear_screen()
    finished = 1
    ingredients = Ingredient.Ingredients()
    print("New recipe\n")
    while finished:
        print("Choosen ingredients")
        print(*ingredients.ingredients, sep='\n')
        print("Add new Ingredient\n")
        print("Name: ")
        name = input()
        print("Amount: ")
        amount = input()
        print("Unit: ")
        unit = input()
        allIngredients.append(Ingredient.Ingredient(name, amount, unit, ingredients))
        print("Finished ? Y/N")
        choice = input()
        if choice == "Y" or choice == "y":
            finished = 0
        else:
            finished = 1
        clear_screen()
    print("Chosen ingredients")
    print(*ingredients.ingredients, sep='\n')
    print("Set name")
    name = input()
    print("Set description")
    description = input()
    print("Type image name")
    image = input()
    return Recipe.Recipe(name, description, ingredients, recipes, image)


def rate_recipe(recipe):
    rate = 6
    while (int(rate) > 5 or int(rate) < 0):
        print("Rate recipe (0 - 5)")
        rate = input()
    recipe.rate(int(rate))


def comment_recipe(recipe):
    print("Type your comment")
    comment = input()
    recipe.add_comment(comment)


def show_recipe():
    if len(recipes.recipes) > 0:
        clear_screen()
        print([o.name for o in recipes.recipes])
        choice = -1
        while not (0 <= int(choice) < len(recipes.recipes)):
            print("Choose recipe ")
            choice = input()
            recipe = recipes.recipes[int(choice)]
        clear_screen()
        print("Recipe chosen\n")
        print(recipe)
        print("1.Rate recipe\n2.Comment recipe\n"
              "3.Show rating\n4.Show comments\nq.Quit")
        choice = input()
        if int(choice) == 1:
            rate_recipe(recipe)
        elif int(choice) == 2:
            comment_recipe(recipe)
        elif int(choice) == 3:
            print(recipe.get_rate())
            input()
        elif int(choice) == 4:
            print(*recipe.comments, sep='\n')
            input()
        elif choice == 'q':
            return
        else:
            print("Invalid input!")
            input()
    else:
        print("No recipes!")
        input()


def show_recipes():
    clear_screen()
    finished = 1
    while finished:
        print([o.name for o in recipes.recipes])
        print("\n1.Add\n2.Delete\n3.Edit\n4.Show recipe \nq.Quit")
        choice = input()
        rec_options = {1: new_recipe,
                       2: del_recipe,
                       3: edit_recipe,
                       4: show_recipe,
                       }
        clear_screen()
        if 'q' == choice:
            finished = 0
        else:
            rec_options[int(choice)]()

        clear_screen()
