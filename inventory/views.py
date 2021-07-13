from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests

# Create your views here.

def index(request):
    url = 'http://127.0.0.1:8000/api/inventory'
    
    res = requests.get(url).json()

    context = {'dash_data' : res}
    
    return render(request, 'index.html', {"items": res})

def detail(request, id):
    url = 'http://127.0.0.1:8000/api/inventory/?name='+id
    
    res = requests.get(url).json()

    context = {'dash_data' : res}
    
    return render(request, 'details.html', {"items": res})