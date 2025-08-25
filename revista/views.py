# revista/views.py

from django.shortcuts import render, get_object_or_404  # Adicione get_object_or_404 aqui
from .models import Editor, Artigo                  # Adicione o modelo Artigo aqui

def corpo_consultivo(request):
    # 1. Busca todos os objetos do tipo Editor no banco de dados
    lista_de_editores = Editor.objects.all()

    # 2. Define o "contexto", que são os dados a serem enviados para o HTML
    contexto = {
        'editores': lista_de_editores
    }

    # 3. Renderiza o arquivo HTML, passando os dados do contexto
    return render(request, 'revista/consultivo.html', contexto)

def artigo_detalhe(request, slug):
    artigo = get_object_or_404(Artigo, slug=slug)
    contexto = {
        'artigo': artigo
    }
    return render(request, 'revista/leia_mais.html', contexto)