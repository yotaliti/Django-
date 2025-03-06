from http.client import HTTPResponse

from django.db.models.expressions import result
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def menu(request, dish):
    recipe = DATA.get(dish)
    servings = int(request.GET.get('servings', 1))
    result_recipe = {}
    if recipe:
        for i in recipe:
            result_recipe[i] = recipe[i] * servings
        context = {
            'recipe': result_recipe
        }
        return render(request, 'calculator/index.html', context)
    return render(request, 'calculator/index.html', {'recipe': {}})

