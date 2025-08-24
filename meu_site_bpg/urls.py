# meu_site_bpg/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings             # Importe settings
from django.conf.urls.static import static   # Importe static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('revista.urls')),
]

# Adicione esta linha no final do arquivo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)