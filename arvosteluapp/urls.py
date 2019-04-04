from django.urls import path
from django.conf.urls import url 
from arvosteluapp.views import list_arvostelut, create_arvostelu, update_arvostelu, delete_arvostelu


urlpatterns = [
    path('', list_arvostelut, name='list_arvostelut'),
    path('new', create_arvostelu, name='create_arvostelu'),
    path('update/<int:id>/', update_arvostelu, name='update_arvostelu'),
    path('delete(<int:id>/', delete_arvostelu, name='delete_arvostelu'),


]