from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:city>/<str:state>/<str:country>/location/', views.location, name='location'),
]

