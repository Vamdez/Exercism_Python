"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)
from sets_categories_data import example_dishes, EXAMPLE_INTERSECTION


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """
    dish_ingredients = set(dish_ingredients)
    recipe = (dish_name, dish_ingredients)
    return recipe


def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) and drink
    name followed by "Cocktail" (includes alcohol).

    """
    drink_ingredients = set(drink_ingredients)
    if drink_ingredients & ALCOHOLS:
        return f'{drink_name} Cocktail'
    else:
        return f'{drink_name} Mocktail'


def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: list - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`

    """
    dish_ingredients = set(dish_ingredients)
    print(dish_ingredients & (VEGAN - (VEGETARIAN | PALEO | OMNIVORE | KETO)))
    if dish_ingredients & (VEGAN - (VEGETARIAN | PALEO | OMNIVORE | KETO)):
        return f'{dish_name}: VEGAN'
    elif dish_ingredients & (VEGETARIAN - (VEGAN | PALEO | OMNIVORE | KETO)):
        return f'{dish_name}: VEGETARIAN'
    elif dish_ingredients & (PALEO - (VEGETARIAN | VEGAN | OMNIVORE | KETO)):
        return f'{dish_name}: PALEO'
    elif dish_ingredients & (KETO - (VEGETARIAN | PALEO | OMNIVORE | VEGAN)):
        return f'{dish_name}: PALEO'
    else:
        return f'{dish_name}: OMNIVORE'


def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: tuple - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """
    res = set()
    for itens in SPECIAL_INGREDIENTS:
        if itens in dish[1]:
            set.add(res, itens)
    return dish[0], res


def compile_ingredients(dishes):
    """Create a master list of ingredients.

    :param dishes: list - of dish ingredient sets.
    :return: set - of ingredients compiled from `dishes`.

    This function should return a `set` of all ingredients from all listed dishes.
    """
    resp = set()
    for c in range(len(dishes)):
        resp |= dishes[c]
    return resp


def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """
    dishes = list(set(dishes))
    for itens in appetizers:
        if itens in dishes:
            dishes.remove(itens)
    return dishes


def singleton_ingredients(dishes, intersection):
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes).

    :param example_dishes: list - of ingredient sets.
    :param EXAMPLE_INTERSECTION: constant - can be one of `<CATEGORY>_INTERSECTION` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTION` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """
    singleton = set()
    for c in range(len(dishes)):
        for itens in dishes[c]:
            if itens not in intersection:
                singleton.add(itens)
    return singleton

