from django.db import models
from core.models.produto import Produto

class Pedido(models.Model):
    produto = models.ManyToManyField(Produto, related_name="pedidos", blank=True)

    def __str__(self):
        return self.produto