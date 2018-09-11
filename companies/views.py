from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from companies.filters import IsOwnerFilterBackend
from companies.models import Company
from companies.permissions import IsOwner
from companies.serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    filter_backends = [IsOwnerFilterBackend]
    permission_classes = [IsOwner]

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
