from django.shortcuts import render
from .models import Recipe
from utils.recipes.factory import make_recipe


def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes_app/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id = category_id).order_by('-id')

    return render(request, 'recipes_app/pages/home.html', context ={
        'recipes':recipes,})

