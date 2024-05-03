from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def result(request):
    return render(request, 'result.html', {})

def recipe(request):
    return render(request, 'recipe.html', {})

def about(request):
    return render(request, 'about.html', {})
