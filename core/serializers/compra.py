from core.views import produto
from rest_framework.serializers import  (
    CharField,
    CurrentUserDefault,
    DateTimeField, # novo
    HiddenField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)
from core.models import Compra, Produto, Endereco
from core.serializers import EnderecoSerializer
from core.serializers.produto import ProdutoSerializer

class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = ("id", "status", "data", "tipo_pagamento") # modificado
