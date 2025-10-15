from django.db import models


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
    link_leia_mais = models.URLField()

    def __str__(self):
        return self.titulo