from . import models, views
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import path

urlpatterns = [
    #path('index/', views.index),
    path('', views.index),
    path('domotic/', views.domotic)
]