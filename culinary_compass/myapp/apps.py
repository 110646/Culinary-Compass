from django.apps import AppConfig

from django import template

register = template.Library()

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
