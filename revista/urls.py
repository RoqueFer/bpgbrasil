from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('artigos/', views.lista_artigos, name='lista_artigos'),
    path('envie-seu-artigo/', views.envie_artigo, name='envie_artigo'),
    path('normas/', views.normas, name='normas'),
    path('consultivo/', views.corpo_consultivo, name='corpo_consultivo'),
    path('fale-conosco/', views.fale_conosco, name='fale_conosco'),
]