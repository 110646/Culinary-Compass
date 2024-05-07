from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect
from django.conf import settings


from .mixins import (
	FormErrors,
	RedirectParams,
	APIMixin
)

'''
Basic view for selecting query
'''
def home(request):

	if request.method == "POST":
		query = request.POST.get("query", None)
		if query:
			return RedirectParams(url = 'myapp:results', params = {"query": query})

	return render(request, 'home.html', {})



'''
Basic view for displaying results
'''
def results(request):

	query = request.GET.get("query", None)

	if query:
		results = APIMixin( query=query).get_data()

		if results:
			context = {
				"results": results,
				"query": query,
			}

			return render(request, 'results.html', context)
	
	return redirect(reverse('myapp:home'))

def details(request):
    return render(request, 'details.html', {})

def about(request):
    return render(request, 'about.html', {})

def top(request):
	return render(request, 'top.html', {})

def tip(request):
	return render(request, 'tip.html', {})