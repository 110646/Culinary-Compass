from django.shortcuts import render, redirect
from django.conf import settings
from urllib.parse import urlencode
import requests

def home(request):
    message = request.GET.get('message', '')
    return render(request, 'home.html', {'message': message})

def results(request):
    query = request.GET.get('query', '')

    if len(query) > 14:
        return redirect(f"/?message=The search exceeds the maximum characters allowed. Please try again.")

    url = f"https://api.spoonacular.com/recipes/complexSearch?query={query}&apiKey={settings.API_KEY}&addRecipeInformation=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])
        if not results:  # Check if the results list is empty
            return redirect(f"/?message=No results found. Please try again.")
        return render(request, 'results.html', {'results': results, 'query': query})
    else:
        return redirect(f"/?message=The number of searches for this site has exceeded. Please try again later.")

def details(request):
    recipe_id = request.GET.get('recipe_id', '')
    query = request.GET.get('query', '')  
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information?includeNutrition=true'
    params = {
        'apiKey': settings.API_KEY,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        recipe_data = response.json()
        if not recipe_data:
            return render(request, 'home.html')
        return render(request, 'details.html', {'recipe': recipe_data, 'query': query})  
    else:
        return render(request, 'home.html')  
        
    
def about(request):
    return render(request, 'about.html', {})

def top(request):
    return render(request, 'top.html', {})

def tip(request):
    return render(request, 'tip.html', {})
