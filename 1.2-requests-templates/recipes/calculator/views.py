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


def assistant(request, name):e
    servings = int(request.GET.get('servings', 1))
    recipe = DATA.get(name).copy()
    for ingredient in recipe:
        recipe[ingredient] *= servings
    context = {
        'recipe': recipe,
    }
    return render(request, 'calculator/index.html', context)
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

# Здравствуйте, Дмитрий! Благодарю за выполненную работу.
# Добавлю пару комментариев как Вы просили)
# Нужно учесть что servings опциональный параметр, а значит его может и не быть в запросе. Этот момент нужно контролировать примерно таким образом:
# if(int(request.GET.get('servings', 1))):
# 	...
# else:
# 	...
