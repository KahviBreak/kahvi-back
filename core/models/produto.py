from django.db import models
from core.models.categoria import Categoria
from core.models.graocafe import Grao


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='produtos')
    estoque = models.IntegerField(default=0)
    # imagem = models.ImageField(upload_to='produtos/')
    grao = models.ForeignKey(Grao, on_delete=models.PROTECT, related_name='produtos', blank=True, null=True)
# fazer uma tabela de grãos (variações de cafe)

    def __str__(self):
        return self.nome
