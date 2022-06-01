from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes_app/home.html')

def contato(request):
    return HttpResponse("Hello Contato!")

def sobre(request):
    return HttpResponse("Hello Sobre")