from django.db import models

class Endereco(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    cep = models.IntegerField()
    bairro = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    numero = models.IntegerField()

    def __str__(self):
        return self.nome