from django.shortcuts import render

DATA = {
    'omlet': {
        'СЏР№С†Р°, С€С‚': 2,
        'РјРѕР»РѕРєРѕ, Р»': 0.1,
        'СЃРѕР»СЊ, С‡.Р».': 0.5,
    },
    'pasta': {
        'РјР°РєР°СЂРѕРЅС‹, Рі': 0.3,
        'СЃС‹СЂ, Рі': 0.05,
    },
    'buter': {
        'С…Р»РµР±, Р»РѕРјС‚РёРє': 1,
        'РєРѕР»Р±Р°СЃР°, Р»РѕРјС‚РёРє': 1,
        'СЃС‹СЂ, Р»РѕРјС‚РёРє': 1,
        'РїРѕРјРёРґРѕСЂ, Р»РѕРјС‚РёРє': 1,
    },
}

def recipe_view(request, dish_name):
    if dish_name in DATA:
        recipe = DATA[dish_name].copy()

        servings = request.GET.get('servings')
        if servings:
            try:
                servings = int(servings)
                for ingredient in recipe:
                    recipe[ingredient] *= servings
            except ValueError:
                pass
        
        context = {
            'recipe': recipe
        }
        return render(request, 'calculator/index.html', context)
    else:
        context = {
            'recipe': {}
        }
        return render(request, 'calculator/index.html', context)