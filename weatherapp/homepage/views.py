from django.shortcuts import render
from django.http import HttpResponse
from dotenv import dotenv_values
import requests

LIMIT = '5'

# Create your views here.
def index(request):
    config = dotenv_values(".env")
    city = 'pittsburgh'
    state = 'PA'
    country = 'USA'
    response = requests.get('http://api.openweathermap.org/geo/1.0/direct?q='+ city 
        +','+ state 
        +','+ country 
        +'&limit='+ LIMIT 
        +'&appid='+ config['OPENWEATHERAPI'])

    print(response.content) 

    return HttpResponse(response.content)