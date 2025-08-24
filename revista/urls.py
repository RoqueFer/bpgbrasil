# revista/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('consultivo/', views.corpo_consultivo, name='corpo_consultivo'),
]