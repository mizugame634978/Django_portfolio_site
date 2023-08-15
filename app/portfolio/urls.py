from django.urls import path
from . import views

app_name= 'portfolio'
urlpatterns = [
    path('', views.index, name='inex'),
    path('works', views.works, name='works'),
]