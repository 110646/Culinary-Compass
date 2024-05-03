from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('results', views.result, name='result'),
    path('recipes', views.recipe, name='recipe'),
    path('about', views.about, name='about')
]
    
