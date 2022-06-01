from django.urls import path
from recipes_app.views import home

urlpatterns = [
    path('', home),
]