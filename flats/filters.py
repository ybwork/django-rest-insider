from django.http import Http404
from rest_framework import filters


class IsOwnerFlatFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        house_owner = request['house'].user

        if request.user == house_owner:
            return queryset.filter(house=house_owner)
        else:
            raise Http404
