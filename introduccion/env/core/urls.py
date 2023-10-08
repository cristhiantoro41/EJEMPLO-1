# En urls.py de tu aplicación o proyecto
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
]

