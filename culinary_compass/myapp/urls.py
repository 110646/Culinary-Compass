from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('results', views.results, name='results'),
    path('details', views.details, name='details'),
    path('about', views.about, name='about')
]
    
