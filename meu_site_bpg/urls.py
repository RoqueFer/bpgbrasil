# meu_site_bpg/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings             # Importe settings
from django.conf.urls.static import static   # Importe static

admin.site.site_header = "BPG Admin"          # Muda o cabeçalho principal
admin.site.site_title = "Administração BPG"   # Muda o título da aba do navegador
admin.site.index_title = "Bem-vindo ao Painel BPG" # Muda o título da página inicial do admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('revista.urls')),
    
]

# Adicione esta linha no final do arquivo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)