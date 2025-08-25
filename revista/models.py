from django.db import models


class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="Texto único para a URL, ex: 'sobre-o-bpg'")
    imagem = models.ImageField(upload_to='artigos/')
    legenda_imagem = models.CharField(max_length=200, blank=True, null=True)
    autor = models.CharField(max_length=100, default="Equipe BPG")
    data_publicacao = models.DateField(auto_now_add=True)
    conteudo = models.TextField()

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
    link_leia_mais = models.URLField()

    def __str__(self):
        return self.titulo