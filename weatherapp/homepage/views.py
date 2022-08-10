from django.shortcuts import render
from django.http import HttpResponse
from dotenv import dotenv_values
import requests

LIMIT = '5'
CONFIG = dotenv_values(".env")

# Create your views here.
def index(request):
    lat, lon = geolocate('pittsburgh', 'PA', 'USA') #testing values
    return HttpResponse(weather(lat, lon))
   
def geolocate(city, state, country):
    response = requests.get('http://api.openweathermap.org/geo/1.0/direct?q='+ city 
        +','+ state 
        +','+ country 
        +'&limit='+ LIMIT 
        +'&appid='+ CONFIG['OPENWEATHERAPI'])

    if (response.status_code != 200):
        return HttpResponse('Error')
    
    response_json = response.json()
    return (response_json[0]['lat'], response_json[0]['lon'])

def weather(lat, lon):
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat='+ str(lat) 
        +'&lon=' + str(lon) 
        +'&appid='+ CONFIG['OPENWEATHERAPI'])

    if (response.status_code != 200):
        return HttpResponse('Error')

    return response.text