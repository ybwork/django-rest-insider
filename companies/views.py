from django.http import Http404
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from buildings.models import Building
from companies.filters import IsOwnerFilterBackend
from companies.models import Company
from companies.serializers import CompanySerializer

company = Company
building = Building


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = company.objects.all()
    filter_backends = [IsOwnerFilterBackend]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class CompanyBuildingsListView(ListAPIView):
    serializer_class = CompanySerializer
    queryset = building.objects.all()

    def get_queryset(self):
        is_user_company = company.objects.filter(
            user_id=self.request.user.id
        ).filter(
            id=self.kwargs['id']
        ).exists()

        if is_user_company:
            return building.objects.filter(company_id=self.kwargs['id'])
        else:
            raise Http404()

