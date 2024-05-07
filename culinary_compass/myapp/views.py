from django.shortcuts import render, redirect
from django.conf import settings
from urllib.parse import urlencode
import requests

def home(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        if query:
            # If a query is provided, redirect to the results page
            return redirect('myapp:results', query=query)
        else:
            # If no query is provided, render the home page template
            return render(request, 'home.html')

def results(request):
    query = request.GET.get('query', '')
    url = f"https://api.spoonacular.com/recipes/complexSearch?query={query}&apiKey={settings.API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])
        return render(request, 'results.html', {'results': results, 'query': query})
    else:
        return render(request, 'results.html', {'results': [], 'query': query})

def details(request):
    recipe_id = request.GET.get('recipe_id', '')
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
    params = {
        'apiKey': settings.API_KEY,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        recipe_data = response.json()
        return render(request, 'details.html', {'recipe': recipe_data})
    else:
        return render(request, 'details.html', {'recipe': None})

def about(request):
    return render(request, 'about.html', {})

def top(request):
	return render(request, 'top.html', {})

def tip(request):
	return render(request, 'tip.html', {})