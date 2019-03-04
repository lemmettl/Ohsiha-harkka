from django.urls import path
from django.conf.urls import url   #autentikointia varten
from . import views
from django.views.generic.base import TemplateView

app_name = 'koirapuistot'

urlpatterns = [
    path('', views.HomePageView, name='kotisivu'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    
]