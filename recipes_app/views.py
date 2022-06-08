from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes_app/pages/home.html', context={'name': 'Marcos Jesus',})

def recipe(request, id):
    return render(request, 'recipes_app/pages/recipe-view.html', context={'name': 'Marcos Jesus',})

