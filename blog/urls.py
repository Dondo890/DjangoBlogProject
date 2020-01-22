from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomePage, name='homepage'),
    path('profile/', views.ProfilePage, name='profile-page'),
]
