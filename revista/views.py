# revista/views.py

from django.shortcuts import render
from .models import Editor # Importe o modelo Editor

def corpo_consultivo(request):
    # 1. Busca todos os objetos do tipo Editor no banco de dados
    lista_de_editores = Editor.objects.all()

    # 2. Define o "contexto", que são os dados a serem enviados para o HTML
    contexto = {
        'editores': lista_de_editores
    }

    # 3. Renderiza o arquivo HTML, passando os dados do contexto
    return render(request, 'revista/consultivo.html', contexto)

def fale_conosco(request):
    return render(request, 'revista/fale_conosco.html')


def home(request):
    return render(request, 'revista/home-page.html')

def lista_artigos(request):
    # Por enquanto, apenas renderiza o template procurePor.html
    return render(request, 'revista/procurePor.html')

def envie_artigo(request):
    # Por enquanto, apenas renderiza o template envie_seu_artigo.html
    return render(request, 'revista/envie_seu_artigo.html')

def normas(request):
    # Por enquanto, apenas renderiza o template normas.html
    return render(request, 'revista/normas.html')