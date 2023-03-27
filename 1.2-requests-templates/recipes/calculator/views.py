from django.shortcuts import render, reverse

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



def home_view(request):
    template_name = 'calculator/home.html'
    menu = {
        'omlet': reverse('omlet'),
        'pasta': reverse('pasta'),
        'buter': reverse('buter'),
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'menu': menu
    }
    return render(request, template_name, context)

def cook(request, st='buter', cnt=2):
    template_name = 'calculator/index.html'
    st=request.path
    st=st[1:-1]
    print(st)

    context = {}
    context['recipe'] = {}
    try:
        for k, v in DATA[st].items():
            context['recipe'][k]=v*cnt
    except:
        context['recipe'] = {}
    return render(request, template_name, context)

