from rest_framework import viewsets

from buildings.models import Building
from buildings.serializers import BuildingSerializer


class BuildingViewSet(viewsets.ModelViewSet):
    serializer_class = BuildingSerializer
    queryset = Building.objects.all()

    # def perform_create(self, serializer):
    #     return serializer.save(request)