# meu_site_bpg/settings.py
import os
from pathlib import Path
from decouple import config # Certifique-se que está importado
import dj_database_url     # <<< ADICIONE ESTA LINHA

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

# IMPORTANTE PARA PRODUÇÃO:
# Ler DEBUG do ambiente, o padrão será False se não definida
DEBUG = config('DEBUG', default=False, cast=bool)

# Ler ALLOWED_HOSTS do ambiente. '*' permite qualquer host (menos seguro, idealmente mude depois)
# ou o Zappa pode gerir isto. Comece com '*' se não tiver a certeza.
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'revista',
    'storages', # <<< ADICIONE 'storages' AQUI
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Não precisamos do WhiteNoise aqui, pois usaremos S3 para estáticos
]

ROOT_URLCONF = 'meu_site_bpg.urls'

TEMPLATES = [ # ... (sem alterações aqui) ... ]

WSGI_APPLICATION = 'meu_site_bpg.wsgi.application'

# --- Configuração do Banco de Dados para AWS RDS ---
DATABASES = {
    'default': dj_database_url.config(
        # Lê a variável de ambiente DATABASE_URL
        default=config('DATABASE_URL'),
        conn_max_age=600 # Opcional: Reutiliza conexões por 10 minutos
    )
}
# Se a variável DATABASE_URL não estiver definida, ele tentará usar um sqlite local
# Certifique-se de que a DATABASE_URL esteja configurada no ambiente Zappa
if not DATABASES['default']:
     DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3', # Fallback para desenvolvimento local
    }


# ... (Validadores de senha, Internacionalização - sem alterações) ...

# --- Configuração de Arquivos Estáticos e Mídia para AWS S3 ---

# Credenciais e Nome do Bucket (serão lidos das variáveis de ambiente no Zappa)
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default=None)
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default=None)
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', default=None)
AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME', default='eu-north-1') # <<< Use a sua região! (Ex: eu-north-1 para Estocolmo)
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'} # Cache de 1 dia nos arquivos

# Configuração para Arquivos Estáticos (coletados pelo collectstatic e servidos pelo S3)
STATIC_LOCATION = 'static' # Nome da pasta dentro do bucket S3
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Configuração para Arquivos de Mídia (uploads do admin salvos no S3)
MEDIA_LOCATION = 'media' # Nome da pasta dentro do bucket S3
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# STATICFILES_DIRS ainda é necessário para o collectstatic encontrar seus arquivos locais
STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# MEDIA_ROOT e STATIC_ROOT não são usados quando se usa S3Boto3Storage