from rest_framework.viewsets import ModelViewSet

from core.models import Grao
from core.serializers import GraoSerializer

class GraoViewSet(ModelViewSet):
    queryset = Grao.objects.all()
    serializer_class = GraoSerializer