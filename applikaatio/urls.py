from django.urls import path, include
from django.conf.urls import url   #autentikointia varten
from . import views
from django.views.generic.base import TemplateView

app_name = 'koirapuistot'

urlpatterns = [
    path('', views.HomePageView, name='kotisivu'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('accounts.urls')),            #url sign up:ia varten, tämä ennen toista accountsia, jotta django lukee ensin tämän
    path('accounts/', include('django.contrib.auth.urls')), 
]