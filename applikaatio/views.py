from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate   #autentikointi
from django.contrib.auth.forms import UserCreationForm  #autentikointi

def HomePageView(request):
    return render(request, 'home.html', {})