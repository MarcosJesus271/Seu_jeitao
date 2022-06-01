from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse("Hello Word!")

def contato(request):
    return HttpResponse("Hello Contato!")

def sobre(request):
    return HttpResponse("Hello Sobre")