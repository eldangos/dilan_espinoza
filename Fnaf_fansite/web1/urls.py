
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),       
    path('home/', views.home, name='home'),
    path('foro/', views.foro, name='foro'),
    path('quest/', views.quest, name='quest'),
    path('quest/', views.quest, name='quest'),
    path('gallery/', views.gallery, name='gallery'),
]