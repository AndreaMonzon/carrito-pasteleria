# Django Imports
from django.urls import path

# App Imports
from . import views


urlpatterns = [
    path('',views.registro, name='Registro'),     
]