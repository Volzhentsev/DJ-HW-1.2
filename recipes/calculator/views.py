from django.shortcuts import render
from django.http import HttpResponse


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
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def main(request):
    return HttpResponse('Рецепты')

def dish_servins(request, recipe):
    servings = int(request.GET.get('servings', 1))
    for ingredient in recipe:
        recipe[ingredient] *= servings
    return recipe

def omlet(request):
    dish = DATA['omlet'].copy()
    omlet = dish_servins(request, dish)
    context = {
        'recipe': omlet
    }
    return render(request, 'calculator/index.html', context)

def pasta(request):
    dish = DATA['pasta'].copy()
    pasta = dish_servins(request, dish)
    context = {
        'recipe': pasta
    }
    return render(request, 'calculator/index.html', context)

def buter(request):
    dish = DATA['buter'].copy()
    buter = dish_servins(request, dish)
    context = {
        'recipe': buter
    }
    return render(request, 'calculator/index.html', context)

