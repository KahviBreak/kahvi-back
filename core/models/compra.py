from django.db import models
from core.models import Produto

class Compra(models.Model):
    class TipoPagemnto(models.IntegerChoices):
        CARTAO_CREDITO = 1, 'Cartão de Crédito'
        CARTAO_DEBITO = 2, 'Cartão de Débito'
        BOLETO = 3, 'Boleto'
        PIX = 4, 'Pix'
        DINHEIRO = 5, 'Dinheiro'
        TRANSFERENCIA_BANCARIA = 6, 'Transferência Bancária'
    
    tipo_pagamento = models.IntegerField(choices=TipoPagemnto.choices)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    produto = models.ManyToManyField(Produto, related_name='produtos')
    # Adicionar relacionamento com o usuário e o produto
    # usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='compras')
    # Adicionar relacionamento com o endereço
    # endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, related_name='compras')
    # Adicionar relacionamento com o grao
    # grao = models.ForeignKey(Grao, on_delete=models.CASCADE, related_name='compras')
    # Adicionar relacionamento com a categoria     


class ItemCompra(models.Model):
    compra = models.ForeignKey('Compra', related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)