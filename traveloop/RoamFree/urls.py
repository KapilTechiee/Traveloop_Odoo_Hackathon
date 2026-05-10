from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("login/", views.login, name='login'),
    path("travel/", views.travel, name='travel'),
    path("trip/", views.trip, name='trip'),
    path("sign/", views.sign, name='sign'),
]