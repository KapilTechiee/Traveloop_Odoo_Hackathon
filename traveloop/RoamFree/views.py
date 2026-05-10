from django.shortcuts import render, redirect
from .models import TravelUser


def home(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        destination = request.POST.get('destination')
        message = request.POST.get('message')

        TravelUser.objects.create(
            name=name,
            email=email,
            destination=destination,
            message=message
        )

        return redirect('home')

    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def travel(request):
    return render(request, 'travel.html')


def trip(request):
    return render(request, 'trip.html')


def sign(request):
    return render(request, 'sign.html')