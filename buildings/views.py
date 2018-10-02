from django.db import IntegrityError
from rest_framework import viewsets

from buildings.filters import IsOwnerFilterBackend
from buildings.models import Building
from buildings.serializers import BuildingSerializer
from buildings.utils import InternalServerError
from companies.models import Company

model = Company


class BuildingViewSet(viewsets.ModelViewSet):
    serializer_class = BuildingSerializer
    queryset = Building.objects.all()
    filter_backends = [IsOwnerFilterBackend]

    def perform_create(self, serializer):
        try:
            company = model.objects.filter(
                user_id=self.request.user.id
            ).filter(
                id=self.request.data['company_id']
            ).first()

            serializer.save(company=company)
        except (KeyError, IntegrityError):
            raise InternalServerError

        return serializer
