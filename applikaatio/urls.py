from django.urls import path, include
from django.conf.urls import url   #autentikointia varten
from . import views

app_name = 'koirapuistot'

urlpatterns =[
    path('', views.HomePageView, name='kotisivu'),
    url('SignUp/', views.signup, name='signup'),
]