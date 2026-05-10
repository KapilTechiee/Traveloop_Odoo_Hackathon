from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.index, name='home'),  # home pageyy
    path("login/", views.login, name='login'),  # login page
]