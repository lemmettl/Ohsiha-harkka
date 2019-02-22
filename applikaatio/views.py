from django.shortcuts import render
from .models import Question
from .models import Choice

def HomePageView(request):
    return render(request, 'index.html', {})

