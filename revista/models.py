from django.db import models
from django.utils.text import slugify

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.CharField(max_length=300)
    doi = models.CharField(max_length=100, blank=True) # Digital Object Identifier
    ano = models.IntegerField()
    volume = models.CharField(max_length=100)
    resumo = models.TextField()
    arquivo_pdf = models.FileField(upload_to='pdfs/') # Descomente depois para uploads

    def __str__(self):
        return self.titulo
    
class Editor(models.Model):
    nome = models.CharField(max_length=150)
    cargo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos_editores/') # Para uploads de imagem

    def __str__(self):
        return self.nome
    

class SlideCarrossel(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='slides/')
    slug = models.SlugField(max_length=110, unique=True, blank=True, help_text="Identificador único para URL (será preenchido automaticamente se deixado em branco)")
    conteudo_detalhado = models.TextField(blank=True, help_text="Conteúdo completo que aparecerá na página 'Leia Mais'.")
    slug = models.SlugField(max_length=110, unique=True, blank=True)    

    def save(self, *args, **kwargs):
        # Gera o slug automaticamente a partir do título se estiver em branco
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
