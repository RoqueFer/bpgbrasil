# revista/views.py

from django.shortcuts import render
from .models import Editor, Artigo, SlideCarrossel # Importe o modelo Editor
from django.shortcuts import render, get_object_or_404 
from django.utils.text import slugify


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
    slides = SlideCarrossel.objects.all()
    context = {'slides': slides}
    return render(request, 'revista/home-page.html', context)
    
# --- FUNÇÃO MODIFICADA ---
def lista_artigos(request):
    # 2. Busca todos os objetos do tipo Artigo no banco de dados
    todos_os_artigos = Artigo.objects.all().order_by('-ano', '-volume') # Ordena por mais recente

    # 3. Cria o contexto com os dados para enviar ao template
    contexto = {
        'artigos': todos_os_artigos
    }

    # 4. Renderiza o template, passando a lista de artigos
    return render(request, 'revista/procurePor.html', contexto)
# -------------------------
def envie_artigo(request):
    # Por enquanto, apenas renderiza o template envie_seu_artigo.html
    return render(request, 'revista/envie_seu_artigo.html')

def normas(request):
    # Por enquanto, apenas renderiza o template normas.html
    return render(request, 'revista/normas.html')

def slide_detalhe(request, slug):
    """
    Exibe a página de detalhes para um slide específico do carrossel.
    """
    slide = get_object_or_404(SlideCarrossel, slug=slug) # Busca o slide pelo slug ou retorna erro 404
    contexto = {
        'slide': slide
    }
    return render(request, 'revista/slide_detalhe.html', contexto)