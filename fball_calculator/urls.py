from django.urls import path, include
from .views import compile,allPlayers
from rest_framework import routers
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('compile', compile, name = 'compile'),
    path('allplayers', allPlayers, name = 'allplayers'),
]