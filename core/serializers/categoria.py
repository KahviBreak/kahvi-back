from rest_framework.serializers import ModelSerializer
from core.models import Categoria
from uploader.serializers import ImageSerializer


class CategoriaSerializer(ModelSerializer):
    imagem = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Categoria
        fields = '__all__'