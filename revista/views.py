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

def home_page(request):

    
    return render(request, 'revista/home-page.html')

def sobre_page(request):
   
    return render(request, 'revista/sobre.html')

def fale_conosco_page(request):
  
    return render(request, 'revista/fale_conosco.html')

def artigos_page(request):
    """
    View para a página de busca de artigos.
    Inicialmente, apenas renderiza o template com os artigos estáticos.
    """
    # No futuro, você buscaria os artigos do banco de dados aqui
    # artigos = Artigo.objects.all()
    # contexto = {'artigos': artigos}
    # return render(request, 'revista/procurePor.html', contexto)

    return render(request, 'revista/procurePor.html')