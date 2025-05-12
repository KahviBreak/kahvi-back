from rest_framework.serializers import ModelSerializer
from core.models import Grao

class GraoSerializer(ModelSerializer):
    class Meta:
        model = Grao
        fields = '__all__'
        # mais tarde alterar fields para não trazer tudo, apenas alguns campos