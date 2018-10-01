from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from companies.filters import IsOwnerFilterBackend
from companies.models import Company
from companies.serializers import CompanySerializer

model = Company


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = model.objects.all()
    filter_backends = [IsOwnerFilterBackend]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class CompanyBuildingsListView(ListAPIView):
    serializer_class = CompanySerializer
    queryset = model.objects.all()
    filter_backends = [IsOwnerFilterBackend]
