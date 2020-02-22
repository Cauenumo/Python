from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	context = {
		'lista1': ['Vitor', 'Pedro', 'André', 'Paulo'],
		'lista2': ['1','2','3'],
		'title': 'Sistemas de Templates e URLs em Django!',
		'paragrafo1': 'Primeiro Parágrafo',
		'paragrafo2': 'Segundo parágrafo'
	}
	return render(request, "index.html", context)

def login(request):
	return render(request, "login.html")