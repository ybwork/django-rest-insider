from rest_framework import viewsets

from flats.models import Flat
from flats.serializers import FlatSerializer


model = Flat


class FlatViewSet(viewsets.ModelViewSet):
    serializer_class = FlatSerializer
    queryset = model.objects.all()
