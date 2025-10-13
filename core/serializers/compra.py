#from core.views import produto
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

#class CompraSerializer(ModelSerializer):
#    class Meta:
#        model = Compra
#        fields = ("id", "produto",) #"status", "data", "tipo_pagamento") # modificado


from core.models import Compra, ItemCompra, Produto
from core.serializers.produto import ProdutoSerializer


class ItemCompraSerializer(ModelSerializer):
    # mostra os dados do produto junto (opcional, pra exibir no GET)
    produto_detalhe = ProdutoSerializer(source='produto', read_only=True)

    class Meta:
        model = ItemCompra
        fields = ['produto', 'produto_detalhe', 'quantidade', 'preco']


class CompraSerializer(ModelSerializer):
    itens = ItemCompraSerializer(many=True)

    class Meta:
        model = Compra
        fields = ['id', 'tipo_pagamento', 'valor', 'data', 'status', 'itens']
        read_only_fields = ['id', 'data']

    def create(self, validated_data):
        itens_data = validated_data.pop('itens', [])
        compra = Compra.objects.create(**validated_data)
        total = 0

        # cria cada item da compra e soma o total
        for item_data in itens_data:
            item = ItemCompra.objects.create(compra=compra, **item_data)
            total += item.preco * item.quantidade

        # atualiza o valor total da compra
        compra.valor = total
        compra.save()

        return compra