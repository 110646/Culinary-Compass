from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('results', views.result, name='result'),
    path('details', views.details, name='details'),
    path('about', views.about, name='about')
]
    
