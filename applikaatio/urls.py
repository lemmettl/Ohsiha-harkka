from django.urls import path
from . import views

app_name = 'kokeilu'

urlpatterns =[
    path('', views.HomePageView, name='kotisivu'),
]