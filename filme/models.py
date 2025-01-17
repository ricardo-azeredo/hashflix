from django.db import models
from django.utils import timezone

# Create your models here.

LISTA_CATEGORIAS = (
    ("ANALISES","Análises"),
    ("PROGRAMACAO","Programação"),
    ("APRESENTACAO","Apresentação"),
    ("OUTROS","Outros")
    
)

class Filme(models.Model):
    titul= models.CharField(max_length=100)
    tumb = models.ImageField(upload_to='tumb_filmes') 
    descriacao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo