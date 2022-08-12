from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<str:city>/<str:state>/<str:country>', views.detail, name='detail'),
]

