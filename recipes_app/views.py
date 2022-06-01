from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes_app/home.html', context={'name': 'Marcos Jesus',})

def contato(request):
    return render(request, 'recipes_app/contato.html')

def sobre(request):
    return HttpResponse("Hello Sobre")