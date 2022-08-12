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
# VIEWS #
def index(request):
    locations_list = list(Location.objects.all())

    latlon_list = []
    x = [latlon_list.append( # this is fairly stupid, needs to be changed
        geolocate(location.city_name, location.state_name, location.country_name)
        ) for location in locations_list]
    weather_list = [] # this is fairly stupid, needs to be changed
    x = [weather_list.append(weather(latlon[0], latlon[1])) for latlon in latlon_list]
    current_weather_list = []
    x = [current_weather_list.append(weather_detail_extractor(weather)) for weather in weather_list]
    
    template = loader.get_template('homepage/index.html')
    context = { # Get rid of redundancy here
        'weather_list': weather_list,
        'current_weather_list': current_weather_list,
    }
        
    return HttpResponse(template.render(context, request))

def location(request, city, state, country): # Figure out default argument for state (not every country has states)
    lat, lon = geolocate(city, state, country)
    current_weather = weather(lat,lon)
    current_weather = weather_detail_extractor(current_weather)

    print(current_weather)
    template = loader.get_template('homepage/search.html')
    context = {
        'current_weather': current_weather,
    }
    return HttpResponse(template.render(context, request))

# HELPER METHODS # 
# Separate these from views.py, create file for helpers
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

def weather_detail_extractor(current_weather):
    return current_weather['weather'][0] | current_weather['main']