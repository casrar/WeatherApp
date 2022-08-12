from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from dotenv import dotenv_values
import requests

from .models import Location

#CONSTANTS
LIMIT = '5'
CONFIG = dotenv_values(".env")

# Create your views here.
def index(request):
    locations_list = list(Location.objects.all())
    latlon_list = []
    x = [latlon_list.append( # this is fairly stupid, needs to be changed
        geolocate(location.city_name, location.state_name, location.country_name)
        ) for location in locations_list]
    weather_list = [] # this is fairly stupid, needs to be changed
    x = [weather_list.append(weather(latlon[0], latlon[1])) for latlon in latlon_list]
    current_weather_list = []
    x = [current_weather_list.append((weather['weather'][0] | weather['main'])) for weather in weather_list]
    
    template = loader.get_template('homepage/index.html')
    context = {
        'weather_list': weather_list,
        'current_weather_list': current_weather_list,
    }
        
    return HttpResponse(template.render(context, request))

def location(request, city, state, country): #figure out default argument for state
    lat, lon = geolocate(city, state, country)
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

    return response.json()