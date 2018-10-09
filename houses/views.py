from rest_framework import viewsets

from houses.filters import IsOwnerHouseFilterBackend
from houses.models import House
from houses.serializers import HouseSerializer

house = House


class HouseViewSet(viewsets.ModelViewSet):
    serializer_class = HouseSerializer
    queryset = house.objects.all()
    filter_backends = [IsOwnerHouseFilterBackend]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
