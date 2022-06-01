from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes_app/home.html', context={'name': 'Marcos Jesus',})

