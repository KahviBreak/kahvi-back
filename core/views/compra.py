from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated  # ← importar isso
from core.models import Compra
from core.serializers.compra import CompraSerializer  # importe direto do arquivo, não do __init__.py

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    permission_classes = [IsAuthenticated]