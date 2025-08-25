# revista/urls.py

from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home_page, name='home'),

    path('consultivo/', views.corpo_consultivo, name='corpo_consultivo'),
    
    path('sobre/', views.sobre_page, name='sobre'),

    path('fale-conosco/', views.fale_conosco_page, name='fale_conosco'),

    path('artigos/', views.artigos_page, name='artigos'),
]