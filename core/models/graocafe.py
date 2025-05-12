from django.db import models
from core.models import categoria
from core.models.categoria import Categoria

class Grao(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    estoque = models.IntegerField(default=0)
    imagem = models.ImageField(upload_to='produtos/')
    intensidade = models.CharField(max_length=255)
    # fazer um select (class) mais tarde para intensidade
    sabor = models.CharField(max_length=255)
    aroma = models.CharField(max_length=255)
    torra = models.CharField(max_length=255)
    # fazer um select (class) mais tarde para intensidade
    acidez = models.CharField(max_length=255)
    corpo = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    variedade = models.CharField(max_length=255)
    processo = models.CharField(max_length=255)
    origem = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='graos', default=None)

    def __str__(self):
        return self.nome
