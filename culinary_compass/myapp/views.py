from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def result(request):
    return render(request, 'result.html', {})

def details(request):
    return render(request, 'detailed.html', {})

def about(request):
    return render(request, 'about.html', {})
