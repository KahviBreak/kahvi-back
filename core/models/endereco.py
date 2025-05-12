from django.db import models

class Endereco(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    cep = models.IntegerField(max_length=8)
    bairro = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    numero = models.IntegerField(max_length=5)

    def __str__(self):
        return self.nome