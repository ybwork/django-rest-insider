from django.http import Http404
from rest_framework import filters

from buildings.utils import InternalServerError
from companies.models import Company

model = Company


class IsOwnerFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        try:
            company = model.objects.filter(
                user_id=request.user.id
            ).filter(
                id=request.data['company_id']
            ).first()
        except KeyError:
            raise InternalServerError

        try:
            queryset.filter(company_id=company.id)
        except AttributeError:
            raise Http404()

        return queryset
